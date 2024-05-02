# ATUC_Artifacts

## Paper
Md Shamimur Rahman, Zadia Codabux and Chanchal K. Roy, "Do Words Have Power? Understanding and Fostering Civility in Code Review Discussion," FSE 2024

## Run Tool
There are two ways to run the prepared detection and translation tool of our above paper"
1. Local machine (please see install.md file for details)
2. Google Co-laboratory (please see colab.md for details)

## Artifacts 
Up-to-date artifacts are available here: [https://github.com/Oyakiolo052/ATUC_Artifacts] 

There are several components in this repository based on our study design.

#### Analysis on [`ToxiCR`](https://dl.acm.org/doi/10.1145/3583562):
This part of this artifact contains a replication of ToxiCR using the BERT model. It also includes the training [`/ATUC_Artifacts/Analysis_on_ToxiCR/code-review-dataset-full.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Analysis_on_ToxiCR/code-review-dataset-full.xlsx) and test [`/ATUC_Artifacts/Analysis_on_ToxiCR/test_ToxiCR.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Analysis_on_ToxiCR/test_ToxiCR.xlsx) set from the original ToxiCR paper. Additionally, we built a new dataset [`/ATUC_Artifacts/Analysis_on_ToxiCR/test_mydata.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/Analysis_on_ToxiCR/test_mydata.xlsx) utilizing ChatGPT and manual analysis. To fine-tune BERT with the training dataset, run the notebook file [`/ATUC_Artifacts/Analysis_on_ToxiCR/classification_civil_uncivil_using_BERT.ipynb`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Analysis_on_ToxiCR/classification_civil_uncivil_using_BERT.ipynb) with the necessary adjustments of the training datapath and also for testing. We shared the fine-tuned ToxiCR model in [`here`](https://doi.org/10.5281/zenodo.10775868), named as ToxiCR_BERT.model. You can find the ToxiCR evaluation using the data [`/ATUC_Artifacts/Analysis_on_ToxiCR/test_mydata.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Analysis_on_ToxiCR/test_mydata.xlsx) we created in this notebook file [`/ATUC_Artifacts/Analysis_on_ToxiCR/Evaluation.ipynb`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Analysis_on_ToxiCR/Evaluation.ipynb).      

#### Refined Detection Model:
[`/ATUC_Artifacts/Refined-detection_model`](https://github.com/Oyakiolo052/ATUC_Artifacts/tree/main/Refined_detection_model) contains the fine-tuned training set [`/ATUC_Artifacts/Refined_detection_model/for_Train_and_validation_data.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Refined_detection_model/for_Train_and_validation_data.xlsx) and testing set [`/ATUC_Artifacts/Refined_detection_model/for_Test_data.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Refined_detection_model/for_Test_data.xlsx) for the refined incivility detection that outperforms [`ToxiCR`](https://dl.acm.org/doi/10.1145/3583562) You can find the finetuned detection model in [`here`](https://doi.org/10.5281/zenodo.10775868), named as "MyModel_BERT.model" under the folder "FineTuned Model." For finetuning from scratch, you can run the notebook file [`/ATUC_Artifacts/Refined_detection_model/classification_civil_uncivil_using_BERT.ipynb`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Refined_detection_model/classification_civil_uncivil_using_BERT.ipynb) with the necessary adjustments to the datapaths. This folder also contains a Python notebook for getting the evaluation metrics (precision, recall, F1-score) [`/ATUC_Artifacts/Refined_detection_model/Evaluation.ipynb`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Refined_detection_model/Evaluation.ipynb).   


