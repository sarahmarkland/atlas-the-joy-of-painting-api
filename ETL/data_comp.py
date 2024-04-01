"""compare titles in each datasets and identify discrepancies in format"""

def read_episode_dates():
    """read & process "Episode Dates" text file"""
    titles = []
    with open('datasets/Episode_Dates.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if '(' in line and ')' in line:
                title, _ = line.strip().split('(')
                titles.append(title.strip())
    return titles

# load the Episode dates dataset
episode_dates_titles = read_episode_dates('datasets/Episode_Dates.txt')

with open('datasets/Colors_Used.csv', 'r', encoding='utf-8') as file:
    colors_used_lines = file.readlines()

with open('datasets/Subject_Matter.csv', 'r', encoding='utf-8') as file:
    subjects_lines = file.readlines()

colors_used_titles = [line.split(',')[0] for line in colors_used_lines]
subject_matter_titles = [line.split(',')[0] for line in subjects_lines]

def standardize_title(title):
    """function to standardize titles"""
    title = title.replace('Mt.', 'Mount').strip()
    return title.title() # convert to title case

# standardize titles
episode_dates_titles = [standardize_title(title) for title in episode_dates_titles]
colors_used_titles = [standardize_title(title) for title in colors_used_titles]
subject_matter_titles = [standardize_title(title) for title in subject_matter_titles]

titles_colors_used = []
titles_subject_matter = []
titles_episode_dates = []
# extract unique titles
episode_dates_titles = set(episode_dates_titles)
colors_used_titles = set(colors_used_titles)
subject_matter_titles = set(subject_matter_titles)

titles_colors_used = set(colors_used_titles)
titles_subject_matter = set(subject_matter_titles)
titles_episode_dates = set(episode_dates_titles)
# find differences
diff_colors_vs_dates = titles_colors_used.difference(titles_episode_dates)
diff_subject_vs_dates = titles_subject_matter.difference(titles_episode_dates)
diff_subject_vs_colors = titles_subject_matter.difference(titles_colors_used.union(titles_episode_dates))

print("Differences - Colors vs Dates:\n", diff_colors_vs_dates)
print("Differences - Subjects vs Dates:\n", diff_subject_vs_dates)
print("Differences - Subjects vs Colors:\n", diff_subject_vs_colors)
