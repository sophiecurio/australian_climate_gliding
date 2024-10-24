import pandas as pd
import glob
import os

# Path to the folder containing the individual OLC files
## olc_scrape.py saves the files in Downloads folder, they need to be moved to the olc_flights folder
folder_path = 'olc_flights/'

# Get a list of all Excel files in the folder
excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

# Sort the files to ensure consistent ordering
excel_files.sort()

# Initialize an empty list to store individual DataFrames
dfs = []

# Loop through each Excel file
for i, file in enumerate(excel_files):
    if i == 0:
        # For the first file, keep the header
        df = pd.read_excel(file)
    else:
        # For subsequent files, skip the header
        df = pd.read_excel(file, header=None, skiprows=1)
        # Set the column names to match the first DataFrame
        df.columns = dfs[0].columns
    
    # Append the DataFrame to our list
    dfs.append(df)

# Concatenate all DataFrames in the list
merged_df = pd.concat(dfs, ignore_index=True)

# Display the first few rows of the merged DataFrame
print(merged_df.head())

merged_df.to_csv("241016olc_flights_all.csv")