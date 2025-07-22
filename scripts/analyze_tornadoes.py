import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ensure output directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Load the filtered tornado data
file_path = "data/tornado_calhoun_2000_2023.csv"
df = pd.read_csv(file_path, dtype=str)

# Convert relevant columns to numeric as needed
df['TOR_F_SCALE'] = pd.to_numeric(df['TOR_F_SCALE'], errors='coerce')
df['INJURIES_DIRECT'] = pd.to_numeric(df['INJURIES_DIRECT'], errors='coerce')
df['DEATHS_DIRECT'] = pd.to_numeric(df['DEATHS_DIRECT'], errors='coerce')
df['DAMAGE_PROPERTY'] = pd.to_numeric(df['DAMAGE_PROPERTY'], errors='coerce')

# Correlation matrix between intensity and damage/injuries
corr_cols = ['TOR_F_SCALE', 'INJURIES_DIRECT', 'DEATHS_DIRECT', 'DAMAGE_PROPERTY']
corr_matrix = df[corr_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix: Tornado Intensity and Damage/Injuries")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "tornado_correlation_heatmap.png"))
plt.close()

# Extract month from BEGIN_DATE_TIME (assumes ISO format 'YYYY-MM-DD HH:MM:SS')
# If format varies, may need to adjust the format string accordingly
df['BEGIN_DATE_TIME'] = pd.to_datetime(df['BEGIN_DATE_TIME'], errors='coerce', infer_datetime_format=True)
df['MONTH'] = df['BEGIN_DATE_TIME'].dt.month

# Count tornadoes by month
monthly_counts = df['MONTH'].value_counts().sort_index()
all_months = range(1,13) # Months 1 to 12

# Reindex monthly_counts to include all months
monthly_counts = df['MONTH'].value_counts().sort_index()
all_months = range(1, 13)
monthly_counts = monthly_counts.reindex(all_months, fill_value=0)

plt.figure(figsize=(10, 6))
sns.barplot(x=list(monthly_counts.index), y=monthly_counts.values, palette='viridis')
plt.xlabel("Month")
plt.ylabel("Number of Tornado Events")
plt.title("Monthly Distribution of Tornado Events (2000-2023)")
plt.xticks(ticks=range(12), labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "tornado_monthly_distribution.png"))
plt.close()


print(f"✅ Correlation heatmap saved to {os.path.join(output_dir, 'tornado_correlation_heatmap.png')}")
print(f"✅ Monthly distribution plot saved to {os.path.join(output_dir, 'tornado_monthly_distribution.png')}")
