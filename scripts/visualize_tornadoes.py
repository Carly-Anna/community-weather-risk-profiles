# scripts/visualize_tornadoes.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import MarkerCluster
import os
import calendar

all_months = range(1, 13)
monthly_counts = monthly_counts.reindex(all_months, fill_value=0)

month_labels = [calendar.month_abbr[m] for m in all_months]  # ['Jan', 'Feb', ..., 'Dec']

plt.figure(figsize=(10,6))
sns.barplot(x=month_labels, y=monthly_counts.values, palette='viridis')
plt.xlabel("Month")
plt.ylabel("Number of Tornado Events")
plt.title("Monthly Distribution of Tornado Events (2000-2023)")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "tornado_monthly_distribution.png"))
plt.close()

# Load data
df = pd.read_csv("data/tornado_calhoun_2000_2023.csv")

# Clean & convert damage to numeric
def parse_damage(val):
    if pd.isna(val):
        return 0
    val = str(val).strip().upper()
    if val.endswith('K'):
        return float(val[:-1]) * 1_000
    elif val.endswith('M'):
        return float(val[:-1]) * 1_000_000
    elif val.endswith('B'):
        return float(val[:-1]) * 1_000_000_000
    else:
        try:
            return float(val)
        except:
            return 0

df["DAMAGE_PROPERTY_NUM"] = df["DAMAGE_PROPERTY"].apply(parse_damage)

# Tornadoes per year
df["YEAR"] = df["BEGIN_YEARMONTH"].astype(str).str[:4].astype(int)
year_counts = df["YEAR"].value_counts().sort_index()

plt.figure(figsize=(10, 5))
sns.barplot(x=year_counts.index, y=year_counts.values, color='skyblue')
plt.title("Tornadoes per Year in Calhoun County (2000–2023)")
plt.xlabel("Year")
plt.ylabel("Tornado Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/tornadoes_per_year.png")
plt.close()

# Tornadoes by intensity
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="TOR_F_SCALE", order=sorted(df["TOR_F_SCALE"].dropna().unique()))
plt.title("Tornado Counts by Fujita/EF Scale")
plt.xlabel("F-Scale")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("outputs/tornadoes_by_intensity.png")
plt.close()

# Total injuries and damage by F-scale
agg = df.groupby("TOR_F_SCALE").agg({
    "INJURIES_DIRECT": "sum",
    "DEATHS_DIRECT": "sum",
    "DAMAGE_PROPERTY_NUM": "sum"
}).fillna(0)

agg.plot(kind="bar", figsize=(10, 6), subplots=True, layout=(3, 1), legend=False, sharex=True)
plt.suptitle("Impact by Tornado Intensity")
plt.xlabel("F-Scale")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("outputs/impact_by_intensity.png")
plt.close()

# Folium Map of Tornado Start Points
map_center = [df["BEGIN_LAT"].mean(), df["BEGIN_LON"].mean()]
m = folium.Map(location=map_center, zoom_start=9)
marker_cluster = MarkerCluster().add_to(m)

for _, row in df.iterrows():
    popup = f"Date: {row['BEGIN_DATE_TIME']}<br>F-Scale: {row['TOR_F_SCALE']}<br>Injuries: {row['INJURIES_DIRECT']}<br>Damage: ${row['DAMAGE_PROPERTY']}"
    folium.Marker(
        location=[row["BEGIN_LAT"], row["BEGIN_LON"]],
        popup=popup
    ).add_to(marker_cluster)

map_path = "outputs/tornado_map.html"
m.save(map_path)
print(f"Map saved to: {map_path}")
