# Netflix Titles - Exploratory Data Analysis

## Project Overview
This project involves exploratory data analysis (EDA) on the Netflix Movies & TV Shows dataset. The goal is to explore the dataset, uncover trends, and visualize key patterns in content distribution, genre popularity, and geographic presence.

## Project Structure
```
Netflix_EDA_Project/
├── dataset/
│   └── netflix_titles.csv
├── notebooks/
│   └── exploratory_data_analysis.ipynb
├── images/
│   ├── content_type_distribution.png
│   ├── top_countries.png
│   ├── top_genres.png
│   └── top_directors.png
├── Netflix_Dataset.py
└── requirements.txt
```

## Key Findings

### Content Type Distribution
- Netflix has significantly more Movies than TV Shows.

### Top Countries
- United States and India are the top producers of Netflix content.

### Top Genres
- International Movies, Dramas, and Comedies are the most common genres.

### Top Directors
- Directors like Rajiv Chilaka and Martin Scorsese frequently appear in the dataset.

## Visualizations
- Content Type Distribution
- Top 10 Countries with Most Titles
- Top 10 Genres
- Top 10 Directors

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn

## Instructions to Run Locally
1. Clone the repository or download the files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Python script:
   ```bash
   python Netflix_Dataset.py
   ```
   Or open the notebook:
   ```bash
   jupyter notebook
   ```

## Conclusion
Netflix's content is heavily skewed toward movies with a strong international and drama genre presence. The platform features contributions from a wide range of countries, with notable representation from the United States and India.

## Future Work
- Build a recommendation engine based on content metadata
- Analyze content trends over time (release year vs. genre)
- Integrate IMDb or Rotten Tomatoes ratings for further analysis
