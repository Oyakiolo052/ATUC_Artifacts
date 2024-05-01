# ATUC_Artifacts

## Paper
Md Shamimur Rahman, Zadia Codabux and Chanchal K. Roy, "Do Words Have Power? Understanding and Fostering Civility in Code Review Discussion," FSE 2024

## Artifacts 
Up-to-date artifacts are available here: [https://github.com/Oyakiolo052/ATUC_Artifacts] 

There are several components in this repository based on our study design.

#### Analysis on [`ToxiCR`](https://dl.acm.org/doi/10.1145/3583562):
This part of this artifact contains a replication of ToxiCR using the BERT model. It also includes the training [`/ATUC_Artifacts/Analysis_on_ToxiCR/code-review-dataset-full.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/Analysis_on_ToxiCR/code-review-dataset-full.xlsx) and test [`/ATUC_Artifacts/Analysis_on_ToxiCR/test_ToxiCR.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/Analysis_on_ToxiCR/test_ToxiCR.xlsx) set from the original ToxiCR paper. Additionally, we built a new dataset [`/ATUC_Artifacts/Analysis_on_ToxiCR/test_mydata.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/Analysis_on_ToxiCR/test_mydata.xlsx) utilizing ChatGPT and manual analysis. To fine-tune BERT with the training dataset, run the notebook file [`/ATUC_Artifacts/Analysis_on_ToxiCR/classification_civil_uncivil_using_BERT.ipynb`](https://github.com/Oyakiolo052/ATUC_Artifacts/Analysis_on_ToxiCR/classification_civil_uncivil_using_BERT.ipynb) with the necessary adjustments of the training datapath and also for testing. We shared the fine-tuned ToxiCR model in [`here`](https://doi.org/10.5281/zenodo.10775868), named as ToxiCR_BERT.model. You can find the ToxiCR evaluation using the data [`/ATUC_Artifacts/Analysis_on_ToxiCR/test_mydata.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/Analysis_on_ToxiCR/test_mydata.xlsx) we created in this notebook file [`/ATUC_Artifacts/Analysis_on_ToxiCR/Evaluation.ipynb`](https://github.com/Oyakiolo052/ATUC_Artifacts/Analysis_on_ToxiCR/Evaluation.ipynb).            



