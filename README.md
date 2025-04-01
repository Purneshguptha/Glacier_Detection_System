Glacier Analysis System
This system provides an interactive interface for analyzing glacier data using Streamlit. Users can upload a CSV dataset containing glacier-related information and visualize key metrics, including distribution, elevation statistics, and risk assessment.

Features
🗺 Interactive web interface using Streamlit

🌍 Visualization of glacier locations on a world map

📊 Statistical analysis of glacier area, elevation, and density

⚠️ Risk assessment based on glacier distribution

🔍 Filtering and detailed data exploration

Setup
1. Install Dependencies
Run the following command to install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt  
2. Prepare Your Data
Ensure your CSV file (database.csv) contains the following columns:

Latitude → Latitude coordinate of the glacier

Longitude → Longitude coordinate of the glacier

Glacier Area → Total area of the glacier (km²)

Minimum Elevation → Lowest elevation of the glacier (m)

Mean Elevation → Average elevation of the glacier (m)

Maximum Elevation → Highest elevation of the glacier (m)

Continent → The continent where the glacier is located

3. Run the Application
Execute the following command to start the application:

bash
Copy
Edit
streamlit run glacier_analysis.py  
Usage
1. Launch the Application
Run the command mentioned above to start the Streamlit interface.

2. Upload Data
Upload your database.csv file through the web interface.

3. Automatic Processing
The system will automatically:
✅ Load and preprocess the data
✅ Generate visualizations of glacier locations and density
✅ Provide statistical insights into glacier elevation and area distribution
✅ Allow filtering and exploration of glacier data

Output
The system provides:
📍 A world map showing glacier locations
📊 Statistical plots of glacier area and elevation distribution
🔥 Density heatmaps of glacier-prone regions
🌍 A continent-wise breakdown of glacier distribution

Technical Details
The system uses:
🔹 Pandas → Data management
🔹 Matplotlib & Seaborn → Data visualization
🔹 Streamlit → Interactive web interface
🔹 Cartopy → Geospatial mapping

Notes
📌 Ensure your CSV file follows the required column format.
📌 Missing or invalid data will be automatically handled.
📌 The application works best with complete and well-structured datasets.

🚀 Enjoy analyzing glaciers!
