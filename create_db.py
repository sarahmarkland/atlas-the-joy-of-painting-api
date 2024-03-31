import psycopg2
# import pandas as pd

dbname='jop_db'
user='postgres'
password='pa$$ord!e'
host='localhost'
port='4321'

create_table_queries = """
    CREATE TABLE IF NOT EXISTS episodes (
        episode_id SERIAL PRIMARY KEY,
        title VARCHAR,
        season INTEGER,
        episode INTEGER,
        colors VARCHAR,
        subjects VARCHAR,
        air_date VARCHAR,
        month VARCHAR,
        notes VARCHAR,
        image_src VARCHAR,
        youtube_src VARCHAR
    )

    CREATE TABLE IF NOT EXISTS episode_colors (
        episode_id INTEGER,
        color_id INTEGER,
        FOREIGN KEY (episode_id) REFERENCES episodes (episode_id),
        FOREIGN KEY (color_id) REFERENCES colors (color_id)
    )

    CREATE TABLE IF NOT EXISTS episode_subjects (
        episode_id INTEGER,
        subject_id INTEGER,
        FOREIGN KEY (episode_id) REFERENCES episodes (episode_id),
        FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
    )

    CREATE TABLE IF NOT EXISTS subjects (
        subject_id SERIAL PRIMARY KEY,
        subject VARCHAR
    )

    CREATE TABLE IF NOT EXISTS colors (
        color_id SERIAL PRIMARY KEY,
        color VARCHAR
    )
]
"""

def create_database():
    """Creates and connects to the database. Returns the connection and cursor to the database."""
    conn = psycopg2.connect(dbname='jop_db', user='postgres', password='pa$$ord!e', host='localhost', port='4321')
    cur = conn.cursor()

    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

    cur.close()
    conn.close()

create_database()
