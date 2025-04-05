# Netflix_Dataset.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

# Load dataset
data = pd.read_csv('dataset/netflix_titles.csv')

# Drop duplicates (if any)
data.drop_duplicates(inplace=True)

# Handle missing values
data['country'] = data['country'].fillna('Unknown')
data['director'] = data['director'].fillna('Not Specified')
data['cast'] = data['cast'].fillna('Not Specified')
data['date_added'] = data['date_added'].fillna(data['date_added'].mode()[0])
data.dropna(subset=['rating', 'duration'], inplace=True)

# Set visualization style
sns.set(style='whitegrid')

# Content type distribution
plt.figure(figsize=(6,4))
sns.countplot(x='type', data=data)
plt.title('Content Type Distribution on Netflix')
plt.savefig('images/content_type_distribution.png')
plt.show()

# Top 10 countries with most content
top_countries = data['country'].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title('Top 10 Countries with Most Netflix Titles')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.savefig('images/top_countries.png')
plt.show()

# Top 10 genres/categories
all_genres = data['listed_in'].str.split(', ')
flat_genres = [genre for sublist in all_genres for genre in sublist]
genre_counts = Counter(flat_genres)
top_genres = dict(genre_counts.most_common(10))

plt.figure(figsize=(10,6))
sns.barplot(x=list(top_genres.values()), y=list(top_genres.keys()))
plt.title('Top 10 Netflix Genres')
plt.xlabel('Frequency')
plt.ylabel('Genre')
plt.savefig('images/top_genres.png')
plt.show()

# Top 10 directors
top_directors = data['director'].value_counts().drop('Not Specified').head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_directors.values, y=top_directors.index)
plt.title('Top 10 Most Frequent Netflix Directors')
plt.xlabel('Number of Titles')
plt.ylabel('Director')
plt.savefig('images/top_directors.png')
plt.show()
