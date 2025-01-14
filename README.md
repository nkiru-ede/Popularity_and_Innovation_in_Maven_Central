## Reproducing Results



### Prerequisites

Install neo4j (version 4.x)

Use Python version 3.*, tested with 3.12.2

### Steps

#### Step 1: Acquire dataset from [Jaime, Damien et al paper](https://dl.acm.org/doi/10.1145/3643991.3644879) paper and convert the database dump to csv using neo4j

| Input | Output |
| --- | --- |
| [Zenodo dataset](https://zenodo.org/records/13734581) | [links_all.csv, release_all.csv](https://zenodo.org/uploads/14184350) |
| Script | script/cypherQuery|

#### Step 2: Merge and clean datasets 

| Script | Input | Output |
| --- | --- | --- |
| `scripts/cleanGoblinData.py`|[links_all.csv, release_all.csv](https://zenodo.org/uploads/14184350) |`cleaned_final_output.csv`


#### Step 3: Aggregate GAV to GA 
| Script | Input | Output |
| --- | --- | --- |
|GAVtoGA.py |  [cleaned_final_output.csv](https://zenodo.org/uploads/14184350)| `plots/GAV_GA_counts`|



#### Step 4: Compute gini
| Script | Input | Output |
| --- | --- | --- |
|giniGA.py |[cleaned_final_output.csv](https://zenodo.org/uploads/14184350)| `plots/gini_GA`|


#### Step 6: Compute top GAs
| Script | Input | Output |
| --- | --- | --- |
| script/top500GAs.py| [cleaned_final_output.csv](https://zenodo.org/uploads/14184350) |top500_per_year |


#### Step 7: Relative change in elites
| Script | Input | Output |
| ---| --- | --- |
| script/eliteChange.py| [top500_per_year.csv](https://zenodo.org/uploads/14184350)  | `plot/FractionOfReplacement_minus2024`|

#### Step 8: Innovation rate
| Script | Input | Output |
| ---| --- | --- |
| script/innovationRate.py| [release_all.csv](https://zenodo.org/uploads/14184350) | `plot/MajorReleaseGA`|








