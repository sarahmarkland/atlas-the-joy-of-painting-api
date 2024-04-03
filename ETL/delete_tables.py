import psycopg2

# connect to the database
conn = psycopg2.connect(
    dbname='sarahmarkland',
    user='postgres',
    password='russwest',
    host='localhost',
    port='4321',
)

# Create a cursor object using the connection
cur = conn.cursor()

# Delete the tables
cur.execute("DROP TABLE episode_colors")
cur.execute("DROP TABLE episode_subjects")
cur.execute("DROP TABLE episodes")
cur.execute("DROP TABLE colors")
cur.execute("DROP TABLE subjects")

# Commit the transaction
conn.commit()

# Close the cursor and the connection
cur.close()
conn.close()
