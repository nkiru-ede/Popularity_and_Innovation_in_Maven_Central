import pandas as pd

yearly_counts = {}

for chunk in pd.read_csv("path to dataset\\cleaned_final_output.csv", chunksize=100000):

    chunk['year'] = chunk['source_release'].str[:4].astype(int)

    chunk['source_ga'] = chunk['source'].str.extract(r'(^[^:]+:[^:]+)')[0]
    chunk['target_ga'] = chunk['target'].str.extract(r'(^[^:]+:[^:]+)')[0]

    chunk = chunk.drop_duplicates(subset=['year', 'source_ga', 'target_ga'])

    yearly_counts_chunk = chunk['year'].value_counts()

    for year, count in yearly_counts_chunk.items():
        yearly_counts[year] = yearly_counts.get(year, 0) + count

aggregated_counts = pd.DataFrame(list(yearly_counts.items()), columns=['year', 'count'])

print(aggregated_counts)