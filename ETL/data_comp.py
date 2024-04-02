"""compare titles in each datasets and identify discrepancies in format"""

def read_episode_dates():
    """read & process "Episode Dates" text file"""
    titles = []
    try:
        with open('datasets/Episode_Dates.txt', 'r', encoding='utf-8') as file:
            for line in file:
                title = line.strip().split('(')[0].strip()
                titles.append(title)
    except FileNotFoundError:
        print("Epidsode Dates file not found")
    return titles

def standardize_title(title):
    """function to standardize titles"""
    title = title.replace('Mt.', 'Mount').strip()
    return title.title() # convert to title case

# load the Episode dates dataset
episode_dates_titles = read_episode_dates()
with open('datasets/Colors_Used.csv', 'r', encoding='utf-8') as file:
    colors_used_lines = file.readlines()
with open('datasets/Subject_Matter.csv', 'r', encoding='utf-8') as file:
    subjects_lines = file.readlines()

# extract titles
colors_used_titles = [line.split(',')[0] for line in colors_used_lines]
subject_matter_titles = [line.split(',')[0] for line in subjects_lines]

# standardize titles
episode_dates_titles = set(standardize_title(title) for title in episode_dates_titles)
colors_used_titles = set(standardize_title(title) for title in colors_used_titles)
subject_matter_titles = set(standardize_title(title) for title in subject_matter_titles)

# find differences
diff_colors_vs_dates = colors_used_titles.difference(episode_dates_titles)
diff_subject_vs_dates = subject_matter_titles.difference(episode_dates_titles)
diff_subject_vs_colors = subject_matter_titles.difference(colors_used_titles)

print("Differences - Colors vs Dates:\n", diff_colors_vs_dates)
print("Differences - Subjects vs Dates:\n", diff_subject_vs_dates)
print("Differences - Subjects vs Colors:\n", diff_subject_vs_colors)
