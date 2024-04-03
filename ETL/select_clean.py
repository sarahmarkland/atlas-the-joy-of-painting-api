# Purpose: Select and clean data from the Colors_Used.csv file
import csv

titles = []
seasons = []
episodes = []
color_lists = []
subjects = []

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

combined_rows = []
for i in range(len(titles)):
    combined_rows.append([titles[i], seasons[i], episodes[i], color_lists[i], subjects[i]])

output_csv = 'clean_data/colors_and_subject_cleandata.csv'
with open(output_csv, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'season', 'episode', 'color_list', 'subject'])
    writer.writerows(combined_rows)
