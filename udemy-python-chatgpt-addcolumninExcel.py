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

        # Add the "annual salary" column in the dataframe
        df['annual_salary'] = df['monthly salary'] * 12

        # Save the updated data back to the Excel file
        writer = pd.ExcelWriter(filepath, engine = 'xlsxwriter')
        df.to_excel(writer, index=False)
        writer.save()