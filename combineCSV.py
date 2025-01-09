import os
import pandas as pd

def combine_csv_files(input_folder, output_file):
    all_files = [file for file in os.listdir(input_folder) if file.endswith('.csv')]
    
    df_list = []

    for i, file in enumerate(all_files):
        file_path = os.path.join(input_folder, file)
        if i == 0:
            df = pd.read_csv(file_path)
        else:
            df = pd.read_csv(file_path, header=0)
        
        df_list.append(df)

    combined_df = pd.concat(df_list, ignore_index=True)

    combined_df.to_csv(output_file, index=False)

    print(f"Combined CSV file saved to {output_file}")


input_folder = 'Phase_2'  
output_file = 'Phase2.csv'       
combine_csv_files(input_folder, output_file)
