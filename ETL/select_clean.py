# Purpose: Select and clean data from the Colors_Used.csv file
import csv

# store titles in a list
titles = []
seasons = []
episodes = []
colors = []

# open the Colors_Used.csv file
with open('datasets/Colors_Used.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    # account for header row
    # headerRow = next(csvreader)
    for row in csvreader:
        title = row['painting_title']
        season = row['season']
        episode = row['episode']
        color_list = row['colors']

    # strip titles and append to list
    # for row in csvreader:
    #     title = row[3]
    #     titles.append(title)
    #     season = row[4]
    #     seasons.append(season)
    #     episode = row[5]
    #     episodes.append(episode)


        # convert string to list
        color_list = color_list.strip("[]").replace("'", "").split(", ")

        titles.append(title)
        seasons.append(season)
        episodes.append(episode)
        colors.append(color_list)

rows = zip(titles, seasons, episodes, colors)


outputcsv = 'clean_data/squeaky.csv'
with open(outputcsv, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([title, season, episode, color_list])
    for row in rows:
        writer.writerow(row)
