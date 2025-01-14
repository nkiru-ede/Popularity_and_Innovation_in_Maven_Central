import pandas as pd

source_target_df = pd.read_csv("path to dataset\\links_all_new.csv") 
artifact_release_df = pd.read_csv("path to dataset\\release_all_new.csv")  

artifact_release_df.rename(columns={'Artifact': 'source'}, inplace=True)

merged_source = pd.merge(source_target_df, artifact_release_df, on='source', how='left')

merged_source.rename(columns={'release': 'source_release'}, inplace=True)

artifact_release_df.rename(columns={'source': 'target'}, inplace=True) 
merged_final = pd.merge(merged_source, artifact_release_df[['target', 'release']], on='target', how='left')

merged_final.rename(columns={'release': 'target_release'}, inplace=True)

merged_final = merged_final.dropna()

merged_final.to_csv("path to dataset\\cleaned_final_output.csv", index=False)


