import os
import pandas as pd

# Define the folder /  directory of source excel files
directory_path = 'udemy-python-chatgpt-excelfiles'

# Loop through each Excel file in the folder
for filename in os.listdir(directory_path):
    if filename.endswith('.xlsx'):
        # Read the excel file into a pandas data frame
        filepath = os.path.join(directory_path, filename)
        df = pd.read_excel(filepath)

        # Add the "monthly tax" and "annual tax" column in the dataframe
        df['monthly tax'] = df['monthly salary'] * 0.10
        df['annual tax'] = df['annual_salary'] * 0.1

        # Save the updated data back to the Excel file
        writer = pd.ExcelWriter(filepath, engine = 'xlsxwriter')
        df.to_excel(writer, index=False)
        writer.save()