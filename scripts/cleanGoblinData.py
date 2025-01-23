import pandas as pd
import os

current_dir = os.getcwd()

source_target_path = os.path.join(current_dir, "links_all_new.csv")
artifact_release_path = os.path.join(current_dir, "release_all_new.csv")
output_path = os.path.join(current_dir, "cleaned_final_output.csv")

source_target_df = pd.read_csv(source_target_path)
artifact_release_df = pd.read_csv(artifact_release_path)

artifact_release_df.rename(columns={'artifact': 'source'}, inplace=True)
merged_source = pd.merge(source_target_df, artifact_release_df, on='source', how='left')
merged_source.rename(columns={'release': 'source_release'}, inplace=True)
artifact_release_df.rename(columns={'source': 'target'}, inplace=True)
merged_final = pd.merge(merged_source, artifact_release_df[['target', 'release']], on='target', how='left')
merged_final.rename(columns={'release': 'target_release'}, inplace=True)
merged_final = merged_final.dropna()

merged_final.to_csv(output_path, index=False)
