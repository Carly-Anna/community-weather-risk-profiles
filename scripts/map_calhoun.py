import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import os
print("Merged columns:", merged.columns.tolist())
print(merged[['STATE', 'CZ_NAME']].drop_duplicates().head(20))

# Ensure output directory exists
os.makedirs("outputs", exist_ok=True)

# Load shapefile and SVI data
shapefile_path = "data/shapefiles/cb_2022_us_county_5m.shp"
counties = gpd.read_file(shapefile_path)
svi = pd.read_csv("data/Alabama_county.csv", dtype={'FIPS': str})

# Merge on FIPS/GEOID
merged = counties.merge(svi, left_on="GEOID", right_on="FIPS")

# Convert CZ_NAME and STATE to uppercase for reliable filtering
merged["CZ_NAME"] = merged["CZ_NAME"].str.upper()
merged["STATE"] = merged["STATE"].str.upper()

# Filter to just Calhoun County, Alabama
calhoun = merged[(merged["CZ_NAME"] == "CALHOUN") & (merged["STATE"] == "ALABAMA")]

if calhoun.empty:
    print("⚠️ No data found for Calhoun County, AL. Check 'CZ_NAME' and 'STATE' columns.")
else:
    print("✅ Calhoun County data loaded successfully.")
    # Loop through each RPL theme and plot
    for i in range(1, 5):
        theme_col = f"RPL_THEME{i}"
        if theme_col not in calhoun.columns:
            print(f"⚠️ Column {theme_col} not found in data. Skipping.")
            continue

        fig, ax = plt.subplots(figsize=(6, 6))
        calhoun.plot(column=theme_col, cmap="OrRd", legend=True, ax=ax, edgecolor='black')
        ax.set_title(f"Calhoun County - {theme_col}")
        ax.axis("off")
        plt.tight_layout()
        output_path = f"outputs/calhoun_{theme_col.lower()}.png"
        plt.savefig(output_path, dpi=300)
        print(f"✅ Saved map: {output_path}")
        plt.close()
