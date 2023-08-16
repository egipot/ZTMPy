import os
import pandas as pd

# Set the directory where the Excel files are located
directory_path = 'udemy-python-chatgpt-excelfiles'

# Create an empty list to store te data from all files
all_data = []

# Loop through each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.xlsx'): #only process Excel files
        # Read the excel file into a pandas DataFrame
        filepath = os.path.join (directory_path, filename)
        data = pd.read_excel(filepath)
        # Append the data to the all_data list
        all_data.append(data)

# Concentrate all the data into a single data frame
merged_data = pd.concat(all_data, ignore_index=True)

# Save the merged data to a new Excel files
merged_data.to_excel('merged_file.xlsx', index=False)

