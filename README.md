# Glacier Retreat Analysis System

This system analyzes and visualizes glacier retreat using time-series satellite images. It provides an interactive interface to upload and analyze satellite imagery data, detect glacier boundaries, and quantify retreat over time.

## Features

- Interactive web interface using Streamlit
- Automated glacier boundary detection using computer vision techniques
- Time-series visualization of glacier retreat
- Quantitative analysis of retreat areas
- Statistical visualization of retreat patterns

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Prepare your data:
   - Create a CSV file (database.csv) with the following columns:
     - image_path: Path to the satellite image
     - date: Date of the image capture

3. Run the application:
```bash
streamlit run glacier_analysis.py
```

## Usage

1. Launch the application using the command above
2. Upload your database.csv file through the web interface
3. The system will automatically:
   - Process all satellite images
   - Detect glacier boundaries
   - Calculate retreat areas
   - Generate visualizations and statistics

## Output

The system provides:
- Original satellite images with detected glacier boundaries
- Time-series visualization of glacier retreat
- Statistical analysis of retreat areas
- Total retreat area calculation

## Technical Details

The system uses:
- OpenCV for image processing and glacier boundary detection
- Pandas for data management
- Matplotlib and Seaborn for visualization
- Streamlit for the interactive web interface

## Notes

- Ensure your satellite images are in a supported format (JPG, PNG)
- The system works best with clear, cloud-free satellite imagery
- Processing time depends on the number and size of images 