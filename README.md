## Reproducing Results



### Prerequisites

1. Install neo4j (version 4.x)
2. Use Python version 3.*, tested with 3.12.2
3. Install the dependencies contained in [requirements.text](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/requirements.txt)

*Note: To install dependencies on MacOS, you may want to use `brew`*


### Steps

#### Step 1: Acquire dataset from [Damien et al: Goblin: A Framework for Enriching and Querying the Maven Central Dependency Graph. MSR'24](https://dl.acm.org/doi/10.1145/3643991.3644879) and convert the database dump to csv

| Script | Input | Output |
| --- | --- | --- |
|[cypherQuery](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/scripts/cypherQuery) |[Goblin dataset](https://doi.org/10.5281/zenodo.10605655)  |[links_all.csv, release_all.csv](https://doi.org/10.5281/zenodo.14184349)


Note: Ensure the converted CSV files `links_all.csv` and `release_all.csv` are saved in your current directory.

#### Step 2: Merge and clean datasets 

| Script | Input | Output |
| --- | --- | --- |
|[cleanGoblinData.py](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/scripts/cleanGoblinData.py)|[links_all.csv, release_all.csv](https://doi.org/10.5281/zenodo.14184349) |[cleaned_final_output.csv](https://doi.org/10.5281/zenodo.14184349)


#### Step 3: Aggregate GAVs to GAs 
| Script | Input | Output |
| --- | --- | --- |
|[GAVtoGA.py](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/scripts/GAVtoGA.py)|  [cleaned_final_output.csv](https://doi.org/10.5281/zenodo.14184349)| [GAV_GA_counts](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/plots/GAV_GA_counts.png)|



#### Step 4: Compute GINIs
| Script | Input | Output |
| --- | --- | --- |
|[giniGA.py](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/scripts/giniGA.py)|[cleaned_final_output.csv](https://doi.org/10.5281/zenodo.14184349)|[gini_GA](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/plots/gini_GA.png)|


#### Step 5: Compute top GAs
| Script | Input | Output |
| --- | --- | --- |
|[top500GAs.py](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/scripts/top500GAs.py)| [cleaned_final_output.csv](https://doi.org/10.5281/zenodo.14184349) |[top500_per_year.csv](https://zenodo.org/uploads/14184350) |


#### Step 6: Relative change in elites
| Script | Input | Output |
| ---| --- | --- |
|[eliteChange.py](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/scripts/eliteChange.py)| [top500_per_year.csv](https://doi.org/10.5281/zenodo.14184349)  |[FractionOfReplacement_minus2024](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/plots/FractionOfReplacement_minus2024.png)|

#### Step 7: Innovation rate
| Script | Input | Output |
| ---| --- | --- |
|[innovationRate.py](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/scripts/innovationRate.py)| [release_all.csv](https://doi.org/10.5281/zenodo.14184349) |[MajorReleaseGA](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/plots/MajorReleaseGA.png)|


## Paper
[Nkiru Ede](https://ecs.wgtn.ac.nz/Main/GradFavourEde), [Jens Dietrich](https://people.wgtn.ac.nz/jens.dietrich), and [Ulrich Zülicke](https://people.wgtn.ac.nz/uli.zuelicke): Popularity and Innovation in Maven Central. [22nd International Conference on Mining Software Repositories (MSR'25), Mining Challenge Track](https://2025.msrconf.org/).






