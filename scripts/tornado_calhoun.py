import pandas as pd
import glob
import os

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Read all yearly CSV files (2000–2023)
csv_files = glob.glob("data/StormEvents_details-ftp_v1.0_d200*_c*.csv")

df_list = []
for f in csv_files:
    print("Reading", f)
    df = pd.read_csv(f, dtype=str, low_memory=False)
    df_list.append(df)

df_all = pd.concat(df_list, ignore_index=True)
df_all['BEGIN_DATE_TIME'] = pd.to_datetime(df_all['BEGIN_DATE_TIME'], errors='coerce')

# Filter by year and event type
df_all = df_all[
    (df_all['BEGIN_DATE_TIME'].dt.year.between(2000, 2023)) &
    (df_all['STATE'] == 'ALABAMA') &
    (df_all['EVENT_TYPE'] == 'Tornado')
]

# Filter for Calhoun County
calhoun = df_all[df_all['CZ_NAME'].str.upper() == 'CALHOUN']

calhoun.to_csv("data/calhoun_tornadoes_2000_2023.csv", index=False)
print(f"✅ Found {len(calhoun)} tornado events in Calhoun County from 2000–2023.")

