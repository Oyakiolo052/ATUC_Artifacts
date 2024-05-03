## Raw GitHub comments from 40 projects:
The collected raw code review comments are available [`here`](https://doi.org/10.5281/zenodo.10775868). Go to the folder "GitHub raw data and predictions" => "Raw_gitHub_projects_comments." You can see 40 .csv files that contain code review comments. The project name is indicated in the file name. 


## Incivility prediction of collected GitHub comments"
The prediction results of raw code review comments are also available [`here`](https://doi.org/10.5281/zenodo.10775868). Go to the folder "GitHub raw data and predictions" => "prediction_using_BERT_github_projectsComment." The column "prediction" indicates 0 for civil and 1 for uncivil comments. 

## Re-evaluate uncivil GitHub comments using [`ToxiCR`](https://dl.acm.org/doi/10.1145/3583562):
We applied ToxiCR to those comments that were predicted as uncivil by our refined incivility detection model. We used these two predictions to compare our refined model with
ToxiCR. Please see [`ATUC_Artifacts/GitHub_dataset/prediction_uncivil_github_comments.csv`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/GitHub_dataset/prediction_uncivil_github_comments.csv)

## Manual Investigation:
We randomly selected 1000 code review comments from that GitHub dataset and applied our refined detection model, ToxiCR, politeness detector and toxicity detector models for the comparative analysis betweeen manual validation and the detectors. Please see [`ATUC_Artifacts/GitHub_dataset/GitHub_dataset/Manual_investigation_Final.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/GitHub_dataset/Manual_investigation_Final.xlsx)

