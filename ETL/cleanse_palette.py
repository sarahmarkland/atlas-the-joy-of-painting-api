import psycopg2
import re
from datetime import datetime

# Connect to postgres DB
conn = psycopg2.connect("dbname=test user=postgres password=secret")

# Open a cursor to perform database operations
cur = conn.cursor()

# Open the file
with open('The Joy Of Painting - Episode Dates.txt', 'r') as file:
    for line in file:
        # Use regex to extract the title and date
        match = re.match(r'"(.+)" \((.+)\)', line)
        if match:
            title, date_str = match.groups()
            # Convert the date string to a datetime object
            date = datetime.strptime(date_str, "%B %d, %Y")
            # Execute the SQL command
            cur.execute("INSERT INTO episodes (title, date) VALUES (%s, %s)", (title, date))

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
