import pandas as pd
import glob

def append_csv_files(output_file_path, input_pattern):
    try:
        all_files = glob.glob(input_pattern)

        dataframes = []
       
        for file in all_files:
            df = pd.read_csv(file)
            dataframes.append(df)
            
        big_dataframe = pd.concat(dataframes, ignore_index=True)
       
        big_dataframe.to_csv(output_file_path, index=False)
        
        print(f"Successfully appended {len(all_files)} CSV files into {output_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

output_file_path = '<File Name>.csv'  # Edit to CSV file name
input_pattern = '<Directory Name>/*.csv'   # Edit to Directory of located csv files
append_csv_files(output_file_path, input_pattern)


