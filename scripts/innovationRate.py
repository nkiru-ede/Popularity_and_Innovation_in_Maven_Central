#InnovationToLastGA - remove last 2 years from plot


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

file_path = "path to dataset\\release_all_new.csv"  
df = pd.read_csv(file_path)

df['ga'] = df['artifact'].apply(lambda x: ':'.join(x.split(':')[:-1]))

df['year'] = df['release'].str[:4].astype(int)

def extract_major_version(artifact):
    try:
        return int(artifact.split(':')[-1].split('.')[0])
    except (IndexError, ValueError):
        return None

df['major_version'] = df['artifact'].apply(extract_major_version)
df = df[df['major_version'].notna()]

df_sorted = df.sort_values(['ga', 'year'])
df_sorted['major_change'] = df_sorted.groupby('ga')['major_version'].diff().fillna(0) > 0

df_innovations = df_sorted[df_sorted['major_change']]
innovation_counts = df_innovations.groupby('year')['ga'].nunique().reset_index(name='Innovation Count')

least_year_ga = df.groupby('ga')['year'].min().reset_index()
least_year_counts = least_year_ga.groupby('year')['ga'].nunique().reset_index(name='First GA Count')

oldest_year_ga = df.groupby('ga')['year'].max().reset_index()
oldest_year_counts = oldest_year_ga.groupby('year')['ga'].nunique().reset_index(name='Last GA Count')

ga_counts = pd.merge(least_year_counts, oldest_year_counts, on='year', how='inner')
ga_counts = pd.merge(ga_counts, innovation_counts, on='year', how='left')
ga_counts['Innovation Count'] = ga_counts['Innovation Count'].fillna(0)  

ga_counts['Innovation1'] = ga_counts['First GA Count'] / ga_counts['Last GA Count']
ga_counts['Innovation2'] = ga_counts['Innovation Count'] / ga_counts['Last GA Count']

start_year = 2002
end_year = 2022
ga_counts_filtered = ga_counts[(ga_counts['year'] >= start_year) & (ga_counts['year'] <= end_year)]

plt.figure(figsize=(10, 6))

plt.plot(ga_counts_filtered['year'], ga_counts_filtered['Innovation1'], marker='o', linestyle='-', color='purple', label='Innovation1 (FirstGA/LastGA)')

plt.plot(ga_counts_filtered['year'], ga_counts_filtered['Innovation2'], marker='o', linestyle='-', color='orange', label='Innovation2 (MajorReleaseGA/LastGA)')

plt.title('Innovation1 vs Innovation2 (2002–2022)')
plt.xlabel('Year')
plt.ylabel('Ratio')

even_years = list(range(start_year, end_year + 1, 2))
plt.xticks(even_years)

plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(integer=True))

plt.grid(True, which="both", linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()

#print(ga_counts_filtered)
