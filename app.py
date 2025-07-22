import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium
import matplotlib.pyplot as plt


@st.cache_data
def load_data():
    # Load tornado data (replace with your file path)
    tornadoes = pd.read_csv("data/tornadoes_calhoun.csv")

    # Load SVI shapefile and CSV
    counties = gpd.read_file("data/shapefiles/cb_2022_us_county_5m.shp")
    svi = pd.read_csv("data/Alabama_county.csv", dtype={'FIPS': str})
    
    # Merge for SVI
    merged = counties.merge(svi, left_on="GEOID", right_on="FIPS")
    calhoun = merged[(merged["STATE"].str.upper() == "ALABAMA") & (merged["COUNTY"].str.upper() == "CALHOUN")]

    return tornadoes, calhoun

tornadoes, calhoun_svi = load_data()

# --- Page title ---
st.title("Community Weather Risk Profile: Calhoun County, Alabama")
st.markdown("""
This dashboard visualizes tornado risk and social vulnerability in Calhoun County from 2000 to 2023.
""")

# --- Section 1: Tornado Overview ---
st.header("1. Tornado Risk Overview")

st.subheader("Tornado Frequency (2000–2023)")
total_tornadoes = len(tornadoes)
st.write(f"Total Tornadoes: **{total_tornadoes}**")

# Tornadoes per year plot
tornadoes['year'] = pd.to_datetime(tornadoes['date']).dt.year
freq = tornadoes.groupby('year').size()

fig, ax = plt.subplots()
freq.plot(kind='bar', ax=ax, color='crimson')
ax.set_xlabel("Year")
ax.set_ylabel("Number of Tornadoes")
ax.set_title("Tornadoes per Year")
st.pyplot(fig)

# --- Section 2: Social Vulnerability Map ---
st.header("2. Social Vulnerability Index (SVI) Themes")

# Folium map of Calhoun county with SVI RPL_THEME1 overlay
m = folium.Map(location=[33.65, -85.83], zoom_start=10)  # Approximate center of Calhoun

# Choropleth for RPL_THEME1 as example
folium.Choropleth(
    geo_data=calhoun_svi,
    data=calhoun_svi,
    columns=['GEOID', 'RPL_THEME1'],
    key_on='feature.properties.GEOID',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.3,
    legend_name='SVI RPL_THEME1 - Socioeconomic Status'
).add_to(m)

st_folium(m, width=700, height=500)

# --- Section 3: Combined Risk Overlay Placeholder ---
st.header("3. Combined Tornado + Vulnerability Risk Overlay")
st.write("*(Coming soon: Interactive overlay map combining tornado data and SVI themes)*")

# --- Section 4: Recommendations ---
st.header("4. Recommendations")
st.markdown(""" 
- Target outreach to mobile home communities  
- Collaborate with local schools and churches for preparedness education  
- Expand NOAA Weather Radio access and app-based alerts  
""")
