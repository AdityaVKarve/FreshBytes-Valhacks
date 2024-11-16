import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# Load the dataset
file_path = '../Data/geo_sensor_locations_bay.csv'  
data = pd.read_csv(file_path)

# Convert the DataFrame to a GeoDataFrame
geometry = [Point(xy) for xy in zip(data['longitude'], data['latitude'])]
geo_data = gpd.GeoDataFrame(data, geometry=geometry)

# Plot using GeoPandas and Matplotlib
fig, ax = plt.subplots(figsize=(10, 10))
geo_data.plot(ax=ax, color='blue', markersize=20)

# Add title and labels
ax.set_title("Sensor Locations", fontsize=16)
ax.set_xlabel("Longitude", fontsize=12)
ax.set_ylabel("Latitude", fontsize=12)

# Show the plot
plt.show()
