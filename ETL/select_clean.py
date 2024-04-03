# # Purpose: Select and clean data from the Colors_Used.csv file
# import csv

# # open the Colors_Used.csv file
# with open('datasets/Colors_Used.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.DictReader(csvfile)

#     # create a list to hold all rows
#     rows = []

#     # account for header row
#     # headerRow = next(csvreader)

#     for row in csvreader:
#         title = row['painting_title']
#         season = row['season']
#         episode = row['episode']
#         color_list = row['colors']

#         # convert string to list
#         color_list = color_list.strip("[]").replace("'", "").split(", ")

#         rows.append([title, season, episode, color_list])

# outputcsv = 'clean_data/squeaky.csv'
# with open(outputcsv, 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow([title, season, episode, color_list])
#     writer.writerows(rows)

# Purpose: Select and clean data from the Colors_Used.csv file
import csv

# Open the Colors_Used.csv file and read data
with open('datasets/Colors_Used.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    # Create a list to hold all rows of data
    rows = []
    # Iterate over each row in the CSV file
    for row in csvreader:
        # Extract values from the current row
        title = row['painting_title']
        season = row['season']
        episode = row['episode']
        colors = row['colors']

        # Convert color list from string to a list of colors
        colors = colors.strip("[]").replace("'", "").split(", ")

        # Append row of data to the list of rows
        rows.append([title, season, episode, colors])

# Write data to a new file
outputcsv = 'clean_data/squeaky.csv'
with open(outputcsv, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    # Write header row
    writer.writerow(['title', 'season', 'episode', 'colors'])
    # Write each row of data
    writer.writerows(rows)
