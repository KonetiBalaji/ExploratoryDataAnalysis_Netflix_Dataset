import pandas as pd

# Load dataset
data = pd.read_csv('./dataset/netflix_titles.csv')

# Preview the first few rows
data.head()

# Dataset structure
data.info()

# Dataset dimensions
print("Shape:", data.shape)

# Summary of missing values
print("Missing values per column:\n", data.isnull().sum())

print("Duplicates:", data.duplicated().sum())
data.drop_duplicates(inplace=True)

# Drop rows where 'rating' or 'duration' is missing (very few rows)
data.dropna(subset=['rating', 'duration'], inplace=True)

# Fill missing 'country' with 'Unknown'
data['country'] = data['country'].fillna('Unknown')

# Fill missing 'director' and 'cast' with 'Not Specified'
data['director'].fillna('Not Specified', inplace=True)
data['cast'].fillna('Not Specified', inplace=True)

# Fill missing 'date_added' with a placeholder or drop — let's use mode (most frequent date)
data['date_added'].fillna(data['date_added'].mode()[0], inplace=True)

# Re-check missing values
print("Missing values after cleaning:\n", data.isnull().sum())

print(data['type'].value_counts())

print(data['country'].value_counts().head(10))

# Since 'listed_in' contains multiple genres, split and count
from collections import Counter

all_genres = data['listed_in'].str.split(', ')
flat_genres = [genre for sublist in all_genres for genre in sublist]
genre_counts = Counter(flat_genres)
print(genre_counts.most_common(10))

print(data['director'].value_counts().head(10))


