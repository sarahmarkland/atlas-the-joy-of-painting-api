# Purpose: Select and clean data from the Colors_Used.csv file
import csv

# open the Colors_Used.csv file
with open('datasets/Colors_Used.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)

    # create a list to hold all rows
    rows = []

    for row in csvreader:
        title = row['painting_title']
        season = row['season']
        episode = row['episode']
        color_list = row['colors']

# Convert string to list and remove '\\r' and '\\n' characters
        color_list = color_list.strip("[]").replace("'", "").replace('\\r', '').replace('\\n', '').split(", ")
        rows.append([title, season, episode, color_list])

outputcsv = 'clean_data/squeaky.csv'
with open(outputcsv, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'season', 'episode', 'color_list'])
    writer.writerows(rows)
