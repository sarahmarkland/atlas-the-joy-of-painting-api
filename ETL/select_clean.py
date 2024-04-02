# Purpose: Select and clean data from the Colors_Used.csv file
import csv

# store titles in a list
titles = []

# open the Colors_Used.csv file
with open('datasets/Colors_Used.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    # account for header row
    headerRow = next(csvreader)

    # strip titles and append to list
    for row in csvreader:
        title = row[3]
        titles.append(title)

# rows = zip(titles...)
outputcsv = 'clean_data/squeaky.csv'
with open(outputcsv, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['title'])
    for title in titles:
        writer.writerow([title])
