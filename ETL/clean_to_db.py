# Purpose: Select and clean data from the Colors_Used.csv file
import csv
import psycopg2

# connect to the database
conn = psycopg2.connect(
    dbname='sarahmarkland',
    user='postgres',
    password='russwest',
    host='localhost',
    port='4321',
)

cur = conn.cursor()

# open the Colors_Used.csv file
with open('datasets/Colors_Used.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)

    # counter for episode_id
    i = 1

    for row in csvreader:
        title = row['painting_title']
        season = row['season']
        episode = row['episode']
        colors = row['colors']

        # Convert string to list and remove '\\r' and '\\n' characters
        colors = colors.strip("[]").replace("'", "").replace('\\r', '').replace('\\n', '').split(", ")

        # insert data into the database
        cur.execute(
            "INSERT INTO episodes (episode_id, title, season, episode, colors) VALUES (%s, %s, %s, %s, %s)",
            (i, title, season, episode, colors)
        )
        i += 1

conn.commit()

cur.close()
conn.close()
