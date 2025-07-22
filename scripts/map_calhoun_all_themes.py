import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load shapefile of US counties
shapefile_path = "data/shapefiles/cb_2022_us_county_5m.shp"
counties = gpd.read_file(shapefile_path)

# Load Alabama SVI data, ensure FIPS is string type
svi = pd.read_csv("data/Alabama_county.csv", dtype={'FIPS': str})

# Merge shapefile and SVI data on GEOID and FIPS
merged = counties.merge(svi, left_on="GEOID", right_on="FIPS")

# Filter for Calhoun County only
calhoun = merged[merged["COUNTY"] == "Calhoun"]

# Set up figure with 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 14))

# List of theme columns and titles
themes = [
    ("RPL_THEME1", "Socioeconomic Vulnerability"),
    ("RPL_THEME2", "Household Composition & Disability"),
    ("RPL_THEME3", "Minority Status & Language"),
    ("RPL_THEME4", "Housing Type & Transportation")
]

# Plot each theme in a subplot
for theme_col, title in themes:
    fig, ax = plt.subplots(figsize=(8, 8))
    calhoun.plot(column=theme_col, cmap="OrRd", legend=True, ax=ax, edgecolor='black')
    ax.set_title(f"Calhoun County, AL - {title} ({theme_col})")
    ax.axis("off")
    plt.tight_layout()
    output_path = f"outputs/calhoun_{theme_col.lower()}.png"
    plt.savefig(output_path, dpi=300)
    print(f"Map saved to {output_path}")
    plt.close(fig)



