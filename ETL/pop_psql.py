import csv
import psycopg2
import re

# connect to the database
conn = psycopg2.connect(
    dbname='sarahmarkland',
    user='postgres',
    password='russwest',
    host='localhost',
    port='4321',
)

cur = conn.cursor()

titles = [] # Colors_Used.csv
seasons = [] # Colors_Used.csv
episodes = [] # Colors_Used.csv
color_lists = [] # Colors_Used.csv
air_dates = [] # Episode_Dates.csv
months = [] # Episode_Dates.csv
subjects = [] # Subject_Matter.csv
colors = [] # Colors_Used.csv

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
        color = row['colors'].strip("[]").replace("'", "").replace('\\r', '').replace('\\n', '').split(", ")

        titles.append(title)
        seasons.append(season)
        episodes.append(episode)
        colors.append(color)

with open('datasets/Episode_Dates.txt', 'r', encoding='utf-8') as dates_file:
    for line in dates_file:
        match = re.search(r'\(([^)]+)', line) # extract text between parentheses
        if match:
            air_date = match.group(1)
            air_dates.append(air_date)
            month = re.search(r'([A-Za-z]+)', air_date).group(1)
            months.append(month)

# combined_rows = []
for i in range(len(titles)):
    cur.execute(
        "INSERT INTO episodes (episode_id, title, season, episode, colors, subjects, air_date, month) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (i + 1, titles[i], seasons[i], episodes[i], colors[i], subjects[i], air_dates[i], months[i])
    )

for i in range(len(color_lists)):
    cur.execute(
        "INSERT INTO colors (color_id, color) VALUES (%s, %s)",
        (i + 1, color[i])
    )

for i in range(len(subjects_list)):
    cur.execute(
        "INSERT INTO subjects (subject_id, subject_name) VALUES (%s, %s)",
        (i + 1, subjects_list[i])
    )

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

# import csv
# import psycopg2
# import re

# # Connect to the database
# conn = psycopg2.connect(
#     dbname='sarahmarkland',
#     user='postgres',
#     password='russwest',
#     host='localhost',
#     port='4321',
# )

# cur = conn.cursor()

# # Define the lists to store data
# titles = []
# seasons = []
# episodes = []
# colors = []
# air_dates = []
# months = []
# subjects = []

# # Open and read the Subject_Matter.csv file
# with open('datasets/Subject_Matter.csv', 'r', encoding='utf-8') as subjects_file:
#     subjects_reader = csv.DictReader(subjects_file)
#     for row in subjects_reader:
#         subjects_list = [column for column, value in row.items() if column != 'TITLE' and value == '1']
#         subjects.append(subjects_list)

# # Open the Colors_Used.csv file
# with open('datasets/Colors_Used.csv', 'r', encoding='utf-8') as colors_file:
#     colors_reader = csv.DictReader(colors_file)
#     for row in colors_reader:
#         title = row['painting_title']
#         season = row['season']
#         episode = row['episode']
#         color = row['colors'].strip("[]").replace("'", "").replace('\\r', '').replace('\\n', '').split(", ")

#         titles.append(title)
#         seasons.append(season)
#         episodes.append(episode)
#         colors.append(color)

# # Open the Episode_Dates.txt file
# with open('datasets/Episode_Dates.txt', 'r', encoding='utf-8') as dates_file:
#     for line in dates_file:
#         match = re.search(r'\(([^)]+)', line) # extract text between parentheses
#         if match:
#             air_date = match.group(1)
#             air_dates.append(air_date)
#             month = re.search(r'([A-Za-z]+)', air_date).group(1)
#             months.append(month)

# # Insert data into the "episodes" table
# for i in range(len(titles)):
#     cur.execute(
#         "INSERT INTO episodes (episode_id, title, season, episode, colors, subjects, air_date, month) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
#         (i + 1, titles[i], seasons[i], episodes[i], colors[i], subjects[i], air_dates[i], months[i])
#     )

# # Insert data into the "colors" table
# for i in range(len(colors)):
#     cur.execute(
#         "INSERT INTO colors (color_id, color_name) VALUES (%s, %s)",
#         (i + 1, color_name[i])
#     )

# # Insert data into the "subjects" table
# for i in range(len(subjects)):
#     for subject_name in subjects[i]:
#         cur.execute(
#             "INSERT INTO subjects (subject_id, subject_name) VALUES (%s, %s)",
#             (i + 1, subject_name)
#         )

# # Commit the changes to the database
# conn.commit()

# # Close the cursor and connection
# cur.close()
# conn.close()
