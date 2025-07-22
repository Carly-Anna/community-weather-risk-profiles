import os
import pandas as pd
import matplotlib.pyplot as plt

# Print working directory
print("Current working directory:", os.getcwd())

# Load the data
df = pd.read_csv("./data/Alabama_county.csv")

# Show available columns
print("Available Columns:")
print(df.columns.tolist())

# Filter for Calhoun County
calhoun_df = df[df['COUNTY'] == "Calhoun"]
print(calhoun_df)

# Select some key SVI percentile rank columns to plot
svi_columns = [
    'EPL_POV150', 'EPL_UNEMP', 'EPL_NOHSDP', 'EPL_UNINSUR',
    'EPL_AGE65', 'EPL_DISABL', 'EPL_MINRTY', 'EPL_MUNIT',
    'EPL_MOBILE', 'EPL_NOVEH'
]

# Get values as a dictionary
svi_values = calhoun_df[svi_columns].iloc[0].to_dict()

# Plot
plt.figure(figsize=(10, 6))
plt.bar(svi_values.keys(), svi_values.values())
plt.xticks(rotation=45, ha='right')
plt.ylabel("SVI Percentile Rank")
plt.title
