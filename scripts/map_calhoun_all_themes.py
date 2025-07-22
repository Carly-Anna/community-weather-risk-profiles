import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure output directory exists
os.makedirs("outputs", exist_ok=True)

# Load shapefile and SVI data
shapefile_path = "data/shapefiles/cb_2022_us_county_5m.shp"
counties = gpd.read_file(shapefile_path)
svi = pd.read_csv("data/Alabama_county.csv", dtype={'FIPS': str})

# Debug: Check columns in SVI CSV
print("SVI CSV columns:", svi.columns.tolist())

# Merge shapefile with SVI on FIPS/GEOID
merged = counties.merge(svi, left_on="GEOID", right_on="FIPS")

# Debug: Show merged columns and sample states/counties
print("Merged columns:", merged.columns.tolist())
print("\nSample STATE and COUNTY values:")
print(merged[['STATE', 'COUNTY']].drop_duplicates().head(10))

# Convert columns to uppercase for consistent filtering
merged["STATE"] = merged["STATE"].str.upper()
merged["COUNTY"] = merged["COUNTY"].str.upper()

# Filter for Calhoun County, Alabama
calhoun = merged[(merged["STATE"] == "ALABAMA") & (merged["COUNTY"] == "CALHOUN")]

if calhoun.empty:
    print("⚠️ No data found for Calhoun County, AL. Check column names or filtering.")
else:
    print("✅ Found data for Calhoun County, AL.")

    # Detect all RPL_THEME columns (1 to 4)
    theme_cols = [col for col in merged.columns if col.startswith("RPL_THEME")]

    if not theme_cols:
        print("⚠️ No RPL_THEME columns found in the data.")
    else:
        print(f"Found theme columns: {theme_cols}")

        # Optional: Map themes to descriptive names if you want
        theme_names = {
            "RPL_THEME1": "Socioeconomic Status",
            "RPL_THEME2": "Household Composition & Disability",
            "RPL_THEME3": "Minority Status & Language",
            "RPL_THEME4": "Housing Type & Transportation"
        }

        for theme_col in sorted(theme_cols):
            vmin = merged[theme_col].min()
            vmax = merged[theme_col].max()
            theme_label = theme_names.get(theme_col, theme_col)

            fig, ax = plt.subplots(figsize=(6, 6))
            calhoun.plot(
                column=theme_col,
                cmap="OrRd",
                legend=True,
                ax=ax,
                edgecolor='black',
                vmin=vmin,
                vmax=vmax,
                legend_kwds={'label': f"{theme_label} (Value)", 'orientation': "vertical"}
            )

            ax.set_title(f"Calhoun County - {theme_label}\nMin: {vmin:.2f}, Max: {vmax:.2f}", fontsize=14)
            ax.axis("off")
            plt.tight_layout()

            output_path = f"outputs/calhoun_{theme_col.lower()}.png"
            plt.savefig(output_path, dpi=300)
            print(f"✅ Saved: {output_path} | {theme_col} min: {vmin}, max: {vmax}")
            plt.close()
