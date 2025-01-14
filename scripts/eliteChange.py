import pandas as pd
import matplotlib.pyplot as plt

file_path = "path to dataset\\top500_per_year.csv" 
df = pd.read_csv(file_path)

df_grouped = df.groupby(['aggregated_artifact', 'dependency_release_year'], as_index=False)['dependency_count'].sum()

plt.figure(figsize=(12, 8))

new_gas_fractions_top_10 = []
new_gas_fractions_top_100 = []
new_gas_fractions_top_500 = []
years = sorted(df_grouped['dependency_release_year'].unique())

years = [year for year in years if year != 2024]

previous_top_10 = set()  
previous_top_100 = set()
previous_top_500 = set()

for year in years:
    year_data = df_grouped[df_grouped['dependency_release_year'] == year]
    
    top_10 = year_data.nlargest(10, 'dependency_count')
    top_100 = year_data.nlargest(100, 'dependency_count')
    top_500 = year_data.nlargest(500, 'dependency_count')
    
    current_top_10 = set(top_10['aggregated_artifact'])
    current_top_100 = set(top_100['aggregated_artifact'])
    current_top_500 = set(top_500['aggregated_artifact'])
    
    new_gas_top_10 = current_top_10 - previous_top_10
    new_gas_top_100 = current_top_100 - previous_top_100
    new_gas_top_500 = current_top_500 - previous_top_500
    
    new_gas_fraction_top_10 = (len(new_gas_top_10) / len(current_top_10)) * 100 if len(current_top_10) > 0 else 0
    new_gas_fraction_top_100 = (len(new_gas_top_100) / len(current_top_100)) * 100 if len(current_top_100) > 0 else 0
    new_gas_fraction_top_500 = (len(new_gas_top_500) / len(current_top_500)) * 100 if len(current_top_500) > 0 else 0
    
    new_gas_fractions_top_10.append(new_gas_fraction_top_10)
    new_gas_fractions_top_100.append(new_gas_fraction_top_100)
    new_gas_fractions_top_500.append(new_gas_fraction_top_500)
    
    print(f"Year: {year}")
    print(f"Top 10: {new_gas_fraction_top_10:.2f}%")
    print(f"Top 100: {new_gas_fraction_top_100:.2f}%")
    print(f"Top 500: {new_gas_fraction_top_500:.2f}%\n")
    
    previous_top_10 = current_top_10
    previous_top_100 = current_top_100
    previous_top_500 = current_top_500

plt.plot(years, new_gas_fractions_top_10, 'b-', label='Top 10')  
plt.plot(years, new_gas_fractions_top_100, 'g-', label='Top 100') 
plt.plot(years, new_gas_fractions_top_500, 'r-', label='Top 500')  
plt.title('Fraction of Replacement in Top 10, Top 100, and Top 500 Over the Years')
plt.xlabel('Year')
plt.ylabel('Fraction of New GAs (%)')
plt.grid(True)
plt.legend(title='GAs', loc='upper right')
plt.xticks(years)
plt.tight_layout()
plt.show()
