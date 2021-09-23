import pandas as pd
import os

df = pd.read_excel('filename.xlsx')
column_name = "Admin_Name"
unique_values = df[column_name].unique()

for unique_values in unique_values:
	df_output=df[df[column_name].str.contains(unique_values)]
	output_path = os.path.join("folder_name", unique_values + '.xlsx')
	df_output.to_excel(output_path, sheet_name=unique_values, index=False)
