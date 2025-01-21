## Reproducing Results



### Prerequisites

Install neo4j (version 4.x)

Use Python version 3.*, tested with 3.12.2

Install the dependencies contained in [requirements.text](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/requirements.txt)

#Note: To install dependencies on MacOs, you may need to use 'brew' command



### Steps

#### Step 1: Acquire dataset from [Jaime, Damien et al paper](https://dl.acm.org/doi/10.1145/3643991.3644879) paper and convert the database dump to csv using neo4j

| Script | Input | Output |
| --- | --- | --- |
|[cypherQuery](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/scripts/cypherQuery) |[Zenodo dataset](https://zenodo.org/records/13734581)  |[links_all.csv, release_all.csv](https://zenodo.org/uploads/14184350)


 

##Note: Ensure the converted csvs links_all.csv and release_all.csv are saved in your current directory.

#### Step 2: Merge and clean datasets 

| Script | Input | Output |
| --- | --- | --- |
|[cleanGoblinData.py](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/scripts/cleanGoblinData.py)|[links_all.csv, release_all.csv](https://zenodo.org/uploads/14184350) |[cleaned_final_output.csv](https://zenodo.org/uploads/14184350)


#### Step 3: Aggregate GAV to GA 
| Script | Input | Output |
| --- | --- | --- |
|[GAVtoGA.py](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/scripts/GAVtoGA.py)|  [cleaned_final_output.csv](https://zenodo.org/uploads/14184350)| [GAV_GA_counts](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/plots/GAV_GA_counts.png)|



#### Step 4: Compute gini
| Script | Input | Output |
| --- | --- | --- |
|[giniGA.py](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/scripts/giniGA.py)|[cleaned_final_output.csv](https://zenodo.org/uploads/14184350)|[gini_GA](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/plots/gini_GA.png)|


#### Step 6: Compute top GAs
| Script | Input | Output |
| --- | --- | --- |
|[top500GAs.py](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/scripts/top500GAs.py)| [cleaned_final_output.csv](https://zenodo.org/uploads/14184350) |[top500_per_year.csv](https://zenodo.org/uploads/14184350) |


#### Step 7: Relative change in elites
| Script | Input | Output |
| ---| --- | --- |
|[eliteChange.py](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/scripts/eliteChange.py)| [top500_per_year.csv](https://zenodo.org/uploads/14184350)  |[FractionOfReplacement_minus2024](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/plots/FractionOfReplacement_minus2024.png)|

#### Step 8: Innovation rate
| Script | Input | Output |
| ---| --- | --- |
|[innovationRate.py](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/scripts/innovationRate.py)| [release_all.csv](https://zenodo.org/uploads/14184350) |[MajorReleaseGA](https://github.com/nkiru-ede/Popularity_and_Innovation_in_Maven_Central/blob/main/plots/MajorReleaseGA.png)|


Paper - Popularity and Innovation in Maven Central.


Authors: Nkiru Ede, Jens Dietrich, and Ulrich Z¨ulicke
{nkiru.ede,jens.dietrich,uli.zuelicke}@vuw.ac.nz
Victoria University of Wellington
Wellington, New Zealand






