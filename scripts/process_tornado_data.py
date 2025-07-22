import pandas as pd
import glob
import os

# Path to data folder
data_path = "data"

# Get list of all StormEvents location CSV files (2000-2023)
files = glob.glob(os.path.join(data_path, "StormEvents_details-ftp_v1.0_d*.csv"))

# Filter files for years 2000-2023
files = [f for f in files if any(str(year) in f for year in range(2000, 2024))]

dfs = []

for file in files:
    print(f"Loading {file}...")
    df = pd.read_csv(file, dtype=str)
    
    # Filter for tornado events
    df = df[df['EVENT_TYPE'] == 'Tornado']
    
    # Filter for Alabama and Calhoun County (STATE == 'ALABAMA', CZ_NAME == 'CALHOUN')
    df = df[(df['STATE'] == 'ALABAMA') & (df['CZ_NAME'] == 'CALHOUN')]
    
    dfs.append(df)

if dfs:
    # Concatenate all years into one DataFrame
    tornado_calhoun = pd.concat(dfs, ignore_index=True)
    print(f"✅ Total tornado events in Calhoun County, AL from 2000-2023: {len(tornado_calhoun)}")

    # Save to CSV
    output_file = os.path.join(data_path, "tornado_calhoun_2000_2023.csv")
    tornado_calhoun.to_csv(output_file, index=False)
    print(f"📊 Saved filtered tornado data to: {output_file}")
else:
    print("⚠️ No tornado data found for Calhoun County.")
