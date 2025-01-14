#GA gini

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_gini_from_csv(file_path):
    def gini_coefficient(x):
        """Compute Gini coefficient for an array x and return Lorenz curve."""
        x = np.array(x, dtype=float)

        x.sort()

        cumulative_sum = np.cumsum(x)

        n = len(x)

        total_sum = cumulative_sum[-1]

        if total_sum == 0:
            return 0.0, None

        lorenz_curve = np.concatenate(([0], cumulative_sum / total_sum))

        gini = 1 - (2 / n) * np.sum(lorenz_curve[1:]) + (1 / n)

        return gini, lorenz_curve

    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    df = df.rename(columns={'source': 'Dependencies', 'target': 'Artifact', 'source_release': 'dependency_release_date', 'target_release': 'artifact_release_date'})
    print(df.head())

    df['dependency_release_year'] = df['dependency_release_date'].str[:4]
    df['artifact_release_year'] = df['artifact_release_date'].str[:4]

    df['dependency_release_year'] = pd.to_numeric(df['dependency_release_year'], errors='coerce')
    
    df = df[df['dependency_release_year'] % 2 == 0]
    
    df['aggregated_artifact'] = df['Artifact'].str.split(':').str[:2].str.join(':')

    artifact_dependency_counts = df.groupby(['aggregated_artifact', 'dependency_release_year'])['Dependencies'].count().reset_index()

    artifact_dependency_counts.rename(columns={'Dependencies': 'dependency_count'}, inplace=True)


    def compute_gini_per_year(df):
        gini_per_year = {}
        lorenz_curves = {}
        for year, group in df.groupby('dependency_release_year'):
            gini, lorenz_curve = gini_coefficient(group['dependency_count'])
            gini_per_year[year] = gini
            lorenz_curves[year] = lorenz_curve
        return gini_per_year, lorenz_curves

    gini_per_year, lorenz_curves = compute_gini_per_year(artifact_dependency_counts)

    plt.figure(figsize=(10, 6))
    for year, lorenz_curve in lorenz_curves.items():
        if lorenz_curve is not None:
            x_values = np.linspace(0, 1, len(lorenz_curve))
            gini_value = gini_per_year[year]
            plt.plot(x_values, lorenz_curve, label=f'Lorenz Curve {year} (Gini: {gini_value:.4f})')

    plt.plot([0, 1], [0, 1], linestyle='--', color='black', label='Line of Equality')

    plt.title('Gini - GA')
    plt.xlabel('Cumulative Share of GA')
    plt.ylabel('Cumulative Share of Dependencies')
    
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    
    plt.grid(True)
    plt.tight_layout() 
    plt.show()

    return gini_per_year

file_path = "path to dataset\\cleaned_final_output.csv"

gini_per_year = calculate_gini_from_csv(file_path)

for year, gini in gini_per_year.items():
    print(f"Gini coefficient for year {year}: {gini:.4f}")
    
    