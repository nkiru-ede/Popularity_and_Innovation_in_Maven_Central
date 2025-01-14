import pandas as pd

def process_artifacts(file_path):
    df = pd.read_csv(file_path, encoding='ISO-8859-1') 

    df['dependency_release_year'] = pd.to_datetime(df['source_release']).dt.year

    df['aggregated_artifact'] = df['target'].str.split(':').str[:2].str.join(':')

    artifact_dependency_counts = df.groupby(['aggregated_artifact', 'dependency_release_year'])['Dependencies'].count().reset_index()

    artifact_dependency_counts.rename(columns={'Dependencies': 'dependency_count'}, inplace=True)

    artifact_dependency_counts = artifact_dependency_counts.sort_values(by=['dependency_release_year', 'dependency_count'], ascending=[True, False])

    return artifact_dependency_counts

def get_top_500_per_year(df):
    top_500_per_year = []
    for year, group in df.groupby('dependency_release_year'):
        top_500_per_year.append(group.head(500))
    return pd.concat(top_500_per_year, ignore_index=True)

def main(input_csv, output_csv):
    processed_df = process_artifacts(input_csv)

    top_500_df = get_top_500_per_year(processed_df)

    top_500_df.to_csv(output_csv, index=False, encoding='ISO-8859-1')

if __name__ == "__main__":
    input_csv = "path to dataset\\cleaned_final_output.csv" 
    output_csv = "top500_per_year.csv" 
    main(input_csv, output_csv)


