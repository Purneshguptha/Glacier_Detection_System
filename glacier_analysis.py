#to run : python -m streamlit run glacier_analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Set page config
st.set_page_config(page_title="Glacier Analysis System", layout="wide")

def load_and_preprocess_data(csv_path):
    """Load and preprocess the glacier data."""
    try:
        # Load data with low_memory=False to handle mixed types
        df = pd.read_csv(csv_path, low_memory=False)
        
        # Convert numeric columns
        numeric_columns = ['Latitude', 'Longitude', 'Glacier Area', 'Minimum Elevation', 
                         'Mean Elevation', 'Maximum Elevation']
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        st.write("Successfully loaded CSV file")
        return df
    except Exception as e:
        st.error(f"Error loading CSV file: {str(e)}")
        return None

def create_world_map(df):
    """Create a world map with glacier locations."""
    fig = plt.figure(figsize=(15, 10))
    ax = plt.axes(projection=ccrs.PlateCarree())
    
    # Add map features
    ax.add_feature(cfeature.LAND, facecolor='lightblue')
    ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
    ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
    ax.add_feature(cfeature.BORDERS, linewidth=0.5)
    
    # Plot glacier locations
    plt.scatter(df['Longitude'], df['Latitude'], 
               color='red', s=20, alpha=0.6, 
               transform=ccrs.PlateCarree())
    
    # Set title and labels
    plt.title('High-Risk Glacier Locations on World Map', pad=20)
    
    # Set map extent to show the whole world
    ax.set_global()
    
    return fig

def create_glacier_analysis(df):
    """Create various analyses of glacier data."""
    try:
        # Create world map with glacier locations
        fig_map = create_world_map(df)
        st.pyplot(fig_map)
        
        # Create a figure with multiple subplots for additional analysis
        fig = plt.figure(figsize=(15, 10))
        
        # 1. Glacier Area Distribution
        plt.subplot(2, 2, 1)
        sns.histplot(data=df, x='Glacier Area', bins=30)
        plt.title('Distribution of Glacier Areas')
        plt.xlabel('Area (km²)')
        
        # 2. Elevation Analysis
        plt.subplot(2, 2, 2)
        elevation_data = df[['Minimum Elevation', 'Mean Elevation', 'Maximum Elevation']].dropna()
        sns.boxplot(data=elevation_data)
        plt.title('Glacier Elevation Statistics')
        plt.ylabel('Elevation (m)')
        
        # 3. Continent Distribution
        plt.subplot(2, 2, 3)
        df['Continent'].value_counts().plot(kind='bar')
        plt.title('Glacier Distribution by Continent')
        plt.xlabel('Continent')
        plt.ylabel('Number of Glaciers')
        
        # 4. Risk Analysis
        plt.subplot(2, 2, 4)
        plt.hist2d(df['Longitude'], df['Latitude'], bins=50, cmap='Reds')
        plt.colorbar(label='Glacier Density')
        plt.title('Glacier Density Map')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        
        plt.tight_layout()
        return fig
    except Exception as e:
        st.error(f"Error creating analysis plots: {str(e)}")
        return None

def main():
    st.title("Glacier Analysis System")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload database.csv", type=['csv'])
    
    if uploaded_file is not None:
        # Load data
        df = load_and_preprocess_data(uploaded_file)
        
        if df is not None and not df.empty:
            # Display basic information
            st.subheader("Dataset Overview")
            st.write(f"Total number of glaciers: {len(df)}")
            st.write(f"Number of continents: {df['Continent'].nunique()}")
            st.write(f"Total glacier area: {df['Glacier Area'].sum():.2f} km²")
            
            # Create tabs for different analyses
            tab1, tab2 = st.tabs(["Statistical Analysis", "Detailed Data"])
            
            with tab1:
                st.subheader("Statistical Analysis")
                analysis_fig = create_glacier_analysis(df)
                if analysis_fig:
                    st.pyplot(analysis_fig)
                
                # Additional statistics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Average Glacier Area", f"{df['Glacier Area'].mean():.2f} km²")
                with col2:
                    st.metric("Average Elevation", f"{df['Mean Elevation'].mean():.0f} m")
                with col3:
                    st.metric("Most Common Continent", df['Continent'].mode()[0])
            
            with tab2:
                st.subheader("Detailed Glacier Data")
                # Add filters
                continent_filter = st.multiselect("Filter by Continent", 
                                                options=sorted(df['Continent'].unique()),
                                                default=sorted(df['Continent'].unique()))
                
                # Apply filters
                filtered_df = df[df['Continent'].isin(continent_filter)]
                
                # Display filtered data
                st.dataframe(filtered_df)

if __name__ == "__main__":
    main() 