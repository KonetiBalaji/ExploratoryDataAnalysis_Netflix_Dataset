# Netflix Titles - Advanced Exploratory Data Analysis

## Project Overview
This project performs comprehensive exploratory data analysis (EDA) on the Netflix Movies & TV Shows dataset. The analysis includes interactive visualizations, temporal trends, content distribution patterns, and detailed insights into Netflix's content library.

## Project Structure
```
Netflix_EDA_Project/
├── dataset/
│   └── netflix_titles.csv
├── images/
│   ├── content_type_distribution.html
│   ├── content_type_distribution.png
│   ├── temporal_analysis.html
│   ├── temporal_analysis.png
│   ├── top_countries.html
│   ├── top_countries.png
│   ├── top_genres.html
│   ├── top_genres.png
│   ├── rating_distribution.html
│   ├── rating_distribution.png
│   ├── duration_analysis.html
│   └── duration_analysis.png
├── Netflix_Dataset.py
├── requirements.txt
└── LICENSE
```

## Features

### Interactive Visualizations
- Content Type Distribution (Interactive Pie Chart)
- Temporal Analysis of Content Addition (Interactive Line Chart)
- Top Countries Analysis (Interactive Bar Chart)
- Genre Distribution (Interactive Bar Chart)
- Rating Distribution (Interactive Pie Chart)
- Duration Analysis (Interactive Box Plot)

### Analysis Components
1. **Content Type Distribution**
   - Distribution of Movies vs TV Shows
   - Interactive pie chart visualization

2. **Temporal Analysis**
   - Content addition trends over time
   - Year-by-year breakdown of content types

3. **Geographic Analysis**
   - Top content-producing countries
   - Country-wise content distribution

4. **Genre Analysis**
   - Most popular genres
   - Genre distribution patterns

5. **Rating Analysis**
   - Distribution of content ratings
   - Rating patterns across different content types

6. **Duration Analysis**
   - Content duration patterns
   - Comparison between Movies and TV Shows

## Technologies Used
- Python 3.x
- Pandas (Data manipulation and analysis)
- NumPy (Numerical computing)
- Plotly (Interactive visualizations)
- Matplotlib & Seaborn (Static visualizations)
- Kaleido (Static image export)

## Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd Netflix_EDA_Project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the analysis script:
```bash
python Netflix_Dataset.py
```

This will generate:
- Interactive HTML visualizations in the `images` directory
- Static PNG visualizations in the `images` directory

## Key Findings

### Content Distribution
- Netflix's content library shows a clear preference for movies over TV shows
- Content addition has shown significant growth over recent years

### Geographic Insights
- United States and India remain the top content producers
- Strong international presence in content creation

### Genre Patterns
- International Movies and Dramas dominate the platform
- Diverse genre representation across different regions

### Content Ratings
- Wide distribution of content ratings
- Family-friendly content forms a significant portion

### Duration Analysis
- Clear distinction between movie and TV show durations
- Consistent patterns in content length across different types

## Future Improvements
- Implement content recommendation system
- Add sentiment analysis of content descriptions
- Integrate with external rating systems (IMDb, Rotten Tomatoes)
- Add machine learning models for content classification
- Implement real-time data updates

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Netflix for providing the dataset
- Open source community for the amazing tools and libraries
