import pandas as pd

file_path = "<File Name>.csv"  # Replace with your CSV file's path
df = pd.read_csv(file_path)

# Grouping by Major Occupation
group_column = "Major Occupation Group"

# Create separate files for each group
for group_name, group_data in df.groupby(group_column):
    
    output_file = f"{group_name}.csv"  # Files will be named based on group name
    group_data.to_csv(output_file, index=False)
    print(f"Created file: {output_file}")
