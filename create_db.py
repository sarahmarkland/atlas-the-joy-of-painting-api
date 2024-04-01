import psycopg2
# import pandas as pd
conn = psycopg2.connect(
    dbname='sarahmarkland',
    user='postgres',
    password='russwest',
    host='localhost',
    port='4321',
)

cur = conn.cursor()

create_table_queries = """
CREATE TABLE "episodes" (
  "episode_id" integer PRIMARY KEY,
  "title" varchar,
  "season" integer,
  "episode" integer,
  "colors" varchar,
  "subjects" varchar,
  "air_date" varchar,
  "month" varchar,
  "notes" varchar,
  "image_src" varchar,
  "youtube_src" varchar
);

CREATE TABLE "episode_colors" (
  "episode_id" integer,
  "color_id" integer
);

CREATE TABLE "episode_subjects" (
  "episode_id" integer,
  "subject_id" integer
);

CREATE TABLE "subjects" (
  "subject_id" integer PRIMARY KEY,
  "subject_name" varchar
);

CREATE TABLE "colors" (
  "color_id" integer PRIMARY KEY,
  "color_name" varchar
);

ALTER TABLE "episode_subjects" ADD FOREIGN KEY ("episode_id") REFERENCES "episodes" ("episode_id");

ALTER TABLE "episode_colors" ADD FOREIGN KEY ("episode_id") REFERENCES "episodes" ("episode_id");

ALTER TABLE "episode_subjects" ADD FOREIGN KEY ("subject_id") REFERENCES "subjects" ("subject_id");

ALTER TABLE "episode_colors" ADD FOREIGN KEY ("color_id") REFERENCES "colors" ("color_id");
"""

# def create_database():
#     """Creates and connects to the database. Returns the connection and cursor to the database."""
#     conn = psycopg2.connect(dbname='sarahmarkland', user='postgres', password='pa$$ord!e', host='localhost', port='4321')
#     cur = conn.cursor()

#     for query in create_table_queries:
#         cur.execute(query)
#         conn.commit()

cur.execute(create_table_queries)

conn.commit()

cur.close()
conn.close()

# create_database()
