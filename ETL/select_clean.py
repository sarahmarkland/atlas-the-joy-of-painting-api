# Purpose: Select and clean data from the Colors_Used.csv file
import csv

# open and read the Subject_Matter.csv file
with open('datasets/Subject_Matter.csv', 'r', encoding='utf-8') as subjects_file:
    subjects_reader = csv.DictReader(subjects_file)

    # Create a dictionary to store the subjects for each episode
    episode_subjects = {}

    # Populate the dictionary with the subjects for each episode
    for row in subjects_reader:
        episode_title = row['TITLE']
        subjects_list = [column for column, value in row.items() if column not in ['EPISODE', 'TITLE'] and value == '1']
        episode_subjects[episode_title] = subjects_list

    print(episode_subjects)

# open the Colors_Used.csv file
with open('datasets/Colors_Used.csv', 'r', encoding='utf-8') as colors_file:
    colors_reader = csv.DictReader(colors_file)
    combined_rows = []

    for row in colors_reader:
        title = row['painting_title']
        season = row['season']
        episode = row['episode']
        color_list = row['colors'].strip("[]").replace("'", "").replace('\\r', '').replace('\\n', '').split(", ")
        subject = ', '.join(episode_subjects.get(episode_title, []))

        print(f"Episode title: {title}, Subject: {subject}")

        combined_rows.append([title, season, episode, color_list, subject])

output_csv = 'clean_data/colors_and_subject_cleandata.csv'
with open(output_csv, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'season', 'episode', 'color_list', 'subject'])
    writer.writerows(combined_rows)
