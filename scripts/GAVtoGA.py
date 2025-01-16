import pandas as pd
import os

current_dir = os.getcwd()

input_file_path = os.path.join(current_dir, "cleaned_final_output.csv")

yearly_counts = {}

for chunk in pd.read_csv(input_file_path, chunksize=100000):
    chunk['year'] = chunk['source_release'].str[:4].astype(int)

    chunk['source_ga'] = chunk['source'].str.extract(r'(^[^:]+:[^:]+)')[0]
    chunk['target_ga'] = chunk['target'].str.extract(r'(^[^:]+:[^:]+)')[0]

    chunk = chunk.drop_duplicates(subset=['year', 'source_ga', 'target_ga'])

    yearly_counts_chunk = chunk['year'].value_counts()

    for year, count in yearly_counts_chunk.items():
        yearly_counts[year] = yearly_counts.get(year, 0) + count

aggregated_counts = pd.DataFrame(list(yearly_counts.items()), columns=['year', 'count'])

print(aggregated_counts)




