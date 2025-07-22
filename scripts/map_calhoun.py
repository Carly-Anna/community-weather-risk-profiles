import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import os

# Make sure output directory exists
os.makedirs("outputs", exist_ok=True)

# Load shapefile of US counties
shapefile_path = "data/shapefiles/cb_2022_us_county_5m.shp"
counties = gpd.read_file(shapefile_path)

# Load Alabama SVI data
svi = pd.read_csv("data/Alabama_county.csv", dtype={'FIPS': str})

# Merge SVI data with shapefile on FIPS/GEOID
merged = counties.merge(svi, left_on="GEOID", right_on="FIPS")

# Filter to just Calhoun County
calhoun = merged[merged["COUNTY"] == "Calhoun"]

# Debug print statements
print(calhoun[['COUNTY', 'RPL_THEME1']])
print(calhoun.geometry)

print(svi[svi['COUNTY'].str.contains("Calhoun", case=False)])
print(merged[merged['COUNTY'].str.contains("Calhoun", case=False)])

# Filter all counties in Alabama
alabama = merged[merged["STATE"] == "Alabama"]

# Plot Alabama map
fig, ax = plt.subplots(figsize=(10, 10))
alabama.plot(column="RPL_THEME1", cmap="OrRd", legend=True, ax=ax, edgecolor='black')
ax.set_title("Alabama Counties - Socioeconomic Vulnerability (RPL_THEME1)")
ax.axis("off")
plt.tight_layout()

# Save Alabama map before showing
plt.savefig("outputs/alabama_svi_map.png", dpi=300)
print("Alabama map saved to outputs/alabama_svi_map.png")
plt.show()

# Plot Calhoun County map
fig, ax = plt.subplots(figsize=(8, 8))
calhoun.plot(column="RPL_THEME1", cmap="OrRd", legend=True, ax=ax, edgecolor='black')
ax.set_title("Calhoun County, AL - Socioeconomic Vulnerability (RPL_THEME1)")
ax.axis("off")
plt.tight_layout()

# Save Calhoun map before showing
plt.savefig("outputs/calhoun_svi_map.png", dpi=300)
print("Calhoun map saved to outputs/calhoun_svi_map.png")
plt.show()
