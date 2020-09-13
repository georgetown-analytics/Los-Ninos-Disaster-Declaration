import glob
import pandas as pd

CHUNK_SIZE = 1000
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
output_file = "../combined_nasa_data.csv"

first_one = True
for csv_file_name in all_filenames:

    if not first_one: # if it is not the first csv file then skip the header row (row 0) of that file
        skip_row = [0]
    else:
        skip_row = []

    chunk_container = pd.read_csv(csv_file_name, chunksize=CHUNK_SIZE, skiprows = skip_row)
    for chunk in chunk_container:
        chunk.to_csv(output_file, mode="a", index=False)
    first_one = False