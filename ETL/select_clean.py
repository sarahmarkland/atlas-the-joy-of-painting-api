# Purpose: Select and clean data from the Colors_Used.csv file
import csv
import re

titles = [] # Colors_Used.csv
seasons = [] # Colors_Used.csv
episodes = [] # Colors_Used.csv
color_lists = [] # Colors_Used.csv
air_dates = [] # Episode_Dates.csv
months = [] # Episode_Dates.csv
subjects = [] # Subject_Matter.csv

# open and read the Subject_Matter.csv file
with open('datasets/Subject_Matter.csv', 'r', encoding='utf-8') as subjects_file:
    subjects_reader = csv.DictReader(subjects_file)

    for row in subjects_reader:
        episode_title = row['TITLE']
        subjects_list = [column for column, value in row.items() if column not in ['EPISODE', 'TITLE'] and value == '1']
        subjects.append(subjects_list)

# open the Colors_Used.csv file
with open('datasets/Colors_Used.csv', 'r', encoding='utf-8') as colors_file:
    colors_reader = csv.DictReader(colors_file)

    for row in colors_reader:
        title = row['painting_title']
        season = row['season']
        episode = row['episode']
        color_list = row['colors'].strip("[]").replace("'", "").replace('\\r', '').replace('\\n', '').split(", ")

        titles.append(title)
        seasons.append(season)
        episodes.append(episode)
        color_lists.append(color_list)

with open('datasets/Episode_Dates.txt', 'r', encoding='utf-8') as dates_file:
    for line in dates_file:
        match = re.search(r'\(([^)]+)', line) # extract text between parentheses
        if match:
            air_date = match.group(1)
            air_dates.append(air_date)
            month = re.search(r'([A-Za-z]+)', air_date).group(1)
            months.append(month)

combined_rows = []
for i in range(len(titles)):
    combined_rows.append([titles[i], seasons[i], episodes[i], color_lists[i], subjects[i], air_dates[i], months[i]])

output_csv = 'clean_data/month_subject_color.csv'
with open(output_csv, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'season', 'episode', 'color_list', 'subject', 'air_date', 'month'])
    writer.writerows(combined_rows)
