"""
Netflix Data Analysis and Visualization
This script performs comprehensive analysis of Netflix content data including
temporal trends, content distribution, and interactive visualizations.
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class NetflixAnalyzer:
    def __init__(self, file_path):
        """Initialize the analyzer with the dataset."""
        self.data = self._load_and_preprocess_data(file_path)
        
    def _load_and_preprocess_data(self, file_path):
        """Load and preprocess the Netflix dataset."""
        # Load data
        data = pd.read_csv(file_path)
        
        # Basic preprocessing
        data.drop_duplicates(inplace=True)
        
        # Handle missing values
        data['country'] = data['country'].fillna('Unknown')
        data['director'] = data['director'].fillna('Not Specified')
        data['cast'] = data['cast'].fillna('Not Specified')
        data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
        data['date_added'] = data['date_added'].fillna(data['date_added'].mode()[0])
        data.dropna(subset=['rating', 'duration'], inplace=True)
        
        # Extract year from date_added
        data['year_added'] = data['date_added'].dt.year
        
        # Clean duration
        data['duration'] = data['duration'].str.extract('(\d+)').astype(float)
        
        return data
    
    def content_type_distribution(self):
        """Analyze and visualize content type distribution."""
        fig = px.pie(self.data, names='type', 
                    title='Content Type Distribution on Netflix',
                    color_discrete_sequence=px.colors.qualitative.Set3)
        fig.write_html('images/content_type_distribution.html')
        fig.write_image('images/content_type_distribution.png')
        
    def temporal_analysis(self):
        """Analyze content addition trends over time."""
        yearly_content = self.data.groupby(['year_added', 'type']).size().reset_index(name='count')
        
        fig = px.line(yearly_content, x='year_added', y='count', color='type',
                     title='Netflix Content Addition Over Time',
                     labels={'year_added': 'Year', 'count': 'Number of Titles'})
        fig.write_html('images/temporal_analysis.html')
        fig.write_image('images/temporal_analysis.png')
        
    def top_countries_analysis(self):
        """Analyze and visualize top content-producing countries."""
        # Split countries and count
        countries = self.data['country'].str.split(', ').explode()
        top_countries = countries.value_counts().head(10)
        
        fig = px.bar(x=top_countries.values, y=top_countries.index,
                    title='Top 10 Countries with Most Netflix Titles',
                    labels={'x': 'Number of Titles', 'y': 'Country'},
                    orientation='h')
        fig.write_html('images/top_countries.html')
        fig.write_image('images/top_countries.png')
        
    def genre_analysis(self):
        """Analyze and visualize genre distribution."""
        genres = self.data['listed_in'].str.split(', ').explode()
        top_genres = genres.value_counts().head(10)
        
        fig = px.bar(x=top_genres.values, y=top_genres.index,
                    title='Top 10 Netflix Genres',
                    labels={'x': 'Frequency', 'y': 'Genre'},
                    orientation='h')
        fig.write_html('images/top_genres.html')
        fig.write_image('images/top_genres.png')
        
    def rating_analysis(self):
        """Analyze and visualize content ratings."""
        rating_counts = self.data['rating'].value_counts()
        
        fig = px.pie(values=rating_counts.values, names=rating_counts.index,
                    title='Distribution of Content Ratings',
                    color_discrete_sequence=px.colors.qualitative.Set3)
        fig.write_html('images/rating_distribution.html')
        fig.write_image('images/rating_distribution.png')
        
    def duration_analysis(self):
        """Analyze content duration patterns."""
        fig = px.box(self.data, x='type', y='duration',
                    title='Content Duration Distribution by Type',
                    labels={'type': 'Content Type', 'duration': 'Duration (minutes)'})
        fig.write_html('images/duration_analysis.html')
        fig.write_image('images/duration_analysis.png')
        
    def run_all_analysis(self):
        """Run all analyses and generate visualizations."""
        print("Starting Netflix data analysis...")
        
        # Create visualizations
        self.content_type_distribution()
        self.temporal_analysis()
        self.top_countries_analysis()
        self.genre_analysis()
        self.rating_analysis()
        self.duration_analysis()
        
        print("Analysis complete! Check the 'images' directory for visualizations.")

def main():
    """Main function to run the analysis."""
    try:
        analyzer = NetflixAnalyzer('dataset/netflix_titles.csv')
        analyzer.run_all_analysis()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
