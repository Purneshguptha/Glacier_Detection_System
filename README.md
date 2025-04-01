Glacier Analysis System
Overview
The Glacier Analysis System is a Streamlit-based web application that provides an interactive interface for analyzing glacier data. It allows users to upload a CSV dataset containing glacier-related information and visualize key metrics, including distribution, elevation statistics, risk assessment, and more.

Features
Upload and preprocess glacier data from CSV files.

Visualize glacier locations on a world map.

Perform statistical analysis of glacier areas, elevations, and distribution across continents.

Generate density maps for high-risk glacier zones.

Filter and explore detailed glacier data interactively.

Installation
Prerequisites
Ensure you have Python 3.7+ installed on your system.

Install Dependencies
Run the following command to install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Running the Application
To launch the Glacier Analysis System, execute:

bash
Copy
Edit
python -m streamlit run glacier_analysis.py
Uploading Data
Upload a CSV file containing glacier information.

The application will preprocess and clean the data.

You will see an overview of key statistics.

Exploring Data
Statistical Analysis: View distributions, box plots, and density maps.

Detailed Data: Filter and analyze glacier records by continent.

Dependencies
The application relies on the following Python libraries:

pandas - Data manipulation

numpy - Numerical computations

matplotlib - Data visualization

seaborn - Enhanced statistical plots

streamlit - Web-based UI

cartopy - Geospatial mapping

opencv-python - Image processing

Pillow - Image handling

folium - Interactive maps

streamlit-folium - Integration with Streamlit

Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests.

License
This project is licensed under the MIT License.
