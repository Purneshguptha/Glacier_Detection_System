# Glacier Analysis System

A comprehensive data visualization and analysis system for studying glacier distributions and characteristics worldwide. This system provides interactive visualizations and statistical analysis of glacier data using Python and Streamlit.

## Features

### 1. Interactive World Map Visualization
- Global visualization of glacier locations
- Color-coded markers showing glacier positions
- Interactive map with country borders and coastlines
- Clear representation of high-risk glacier areas

### 2. Statistical Analysis
- Distribution of glacier areas
- Elevation statistics (minimum, mean, maximum)
- Continental distribution analysis
- Glacier density heatmap
- Key metrics and averages

### 3. Data Exploration
- Interactive data filtering by continent
- Detailed data table view
- Sortable and searchable data columns
- Comprehensive dataset overview

## Installation

1. Clone this repository:
```bash
git clone [https://github.com/Purneshguptha/Glacier_Detection_System.git]
cd glacier-analysis-system
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

Required packages:
- pandas
- numpy
- matplotlib
- seaborn
- streamlit
- cartopy

## Usage

1. Start the Streamlit application:
```bash
python -m streamlit run glacier_analysis.py
```

2. Open your web browser and navigate to:
```
http://localhost:8501
```

3. Upload your glacier database CSV file containing the following columns:
   - Glacier ID
   - Political Unit
   - Continent
   - Latitude
   - Longitude
   - Glacier Area
   - Minimum Elevation
   - Mean Elevation
   - Maximum Elevation
   - Glacier Name

## Data Visualization

The system provides multiple visualization types:

1. **World Map View**
   - Interactive global map showing glacier locations
   - Red markers indicating glacier positions
   - Light blue background for clear visibility

2. **Statistical Plots**
   - Glacier area distribution histogram
   - Elevation statistics box plots
   - Continental distribution bar chart
   - Glacier density heat map

3. **Metrics Dashboard**
   - Average glacier area
   - Average elevation
   - Most common continent
   - Total number of glaciers
   - Total glacier area

## Data Requirements

Your CSV file should contain the following columns:
- Required columns: Latitude, Longitude, Glacier Area, Continent
- Optional but recommended: Minimum Elevation, Mean Elevation, Maximum Elevation, Glacier Name

## Technical Details

- Built with Python 3.x
- Uses Streamlit for web interface
- Cartopy for map visualization
- Pandas for data processing
- Matplotlib and Seaborn for statistical plots

## Notes

- First-time run may require downloading map data files
- Large datasets may take a few moments to process
- Recommended screen resolution: 1920x1080 or higher for optimal visualization

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
