# ATUC_Artifacts

## Paper
Md Shamimur Rahman, Zadia Codabux and Chanchal K. Roy, "Do Words Have Power? Understanding and Fostering Civility in Code Review Discussion," FSE 2024

## Run Tool
There are two ways to run the prepared detection and translation tool of our above paper"
1. Local machine (please see [`/ATUC_Artifacts/install.md`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/install.md) file for details)
2. Google Co-laboratory (please see [`/ATUC_Artifacts/colab.md`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/colab.md) for details)

## Artifacts 
Up-to-date artifacts are available here: [https://github.com/Oyakiolo052/ATUC_Artifacts] 

There are several components in this repository based on our study design.

#### Analysis on [`ToxiCR`](https://dl.acm.org/doi/10.1145/3583562):
This part of this artifact contains a replication of ToxiCR using the BERT model. It also includes the training [`/ATUC_Artifacts/Analysis_on_ToxiCR/code-review-dataset-full.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Analysis_on_ToxiCR/code-review-dataset-full.xlsx) and test [`/ATUC_Artifacts/Analysis_on_ToxiCR/test_ToxiCR.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Analysis_on_ToxiCR/test_ToxiCR.xlsx) set from the original ToxiCR paper. Additionally, we built a new dataset [`/ATUC_Artifacts/Analysis_on_ToxiCR/test_mydata.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/Analysis_on_ToxiCR/test_mydata.xlsx) utilizing ChatGPT and manual analysis. To fine-tune BERT with the training dataset, run the notebook file [`/ATUC_Artifacts/Analysis_on_ToxiCR/classification_civil_uncivil_using_BERT.ipynb`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Analysis_on_ToxiCR/classification_civil_uncivil_using_BERT.ipynb) with the necessary adjustments of the training datapath and also for testing. We shared the fine-tuned ToxiCR model in [`here`](https://doi.org/10.5281/zenodo.10775868), named as ToxiCR_BERT.model. You can find the ToxiCR evaluation using the data [`/ATUC_Artifacts/Analysis_on_ToxiCR/test_mydata.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Analysis_on_ToxiCR/test_mydata.xlsx) we created in this notebook file [`/ATUC_Artifacts/Analysis_on_ToxiCR/Evaluation.ipynb`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Analysis_on_ToxiCR/Evaluation.ipynb).      

#### Refined Detection Model:
[`/ATUC_Artifacts/Refined-detection_model`](https://github.com/Oyakiolo052/ATUC_Artifacts/tree/main/Refined_detection_model) contains the fine-tuned training set [`/ATUC_Artifacts/Refined_detection_model/for_Train_and_validation_data.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Refined_detection_model/for_Train_and_validation_data.xlsx) and testing set [`/ATUC_Artifacts/Refined_detection_model/for_Test_data.xlsx`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Refined_detection_model/for_Test_data.xlsx) for the refined incivility detection that outperforms [`ToxiCR`](https://dl.acm.org/doi/10.1145/3583562) You can find the finetuned detection model in [`here`](https://doi.org/10.5281/zenodo.10775868), named as "MyModel_BERT.model" under the folder "FineTuned Model." For finetuning from scratch, you can run the notebook file [`/ATUC_Artifacts/Refined_detection_model/classification_civil_uncivil_using_BERT.ipynb`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Refined_detection_model/classification_civil_uncivil_using_BERT.ipynb) with the necessary adjustments to the datapaths. This folder also contains a Python notebook for getting the evaluation metrics (precision, recall, F1-score) [`/ATUC_Artifacts/Refined_detection_model/Evaluation.ipynb`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Refined_detection_model/Evaluation.ipynb).   

We also conducted a comparative analysis of our refined model and the existing ones. Please have a look at [`/ATUC_Artifacts/GitHub_dataset/ReadMe.md`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/GitHub_dataset/ReadMe.md) for details.

#### Translation Models:
We used three versions of T5 (i.e., small, base, and large), two versions of BART (i.e., base and large), MarianMT, NLLB, and GPT 3.5. If you want to finetune all the models from scratch, then go for the files with plain names. For example, for fine-tuned the T5, go [`/ATUC_Artifacts/Translation_model/T5.ipynb`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Translation_model/T5.ipynb). You need to adjust the datapath and mention the T5 versions (i.e., T5-small, T5-base and T5-large). For fine-tuning, we used the dataset [`/ATUC_Artifacts/Translation_model/uncivil_to_civil.csv`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Translation_model/uncivil_to_civil.csv) containing uncivil comments and their civil counterparts. For GPT3.5, we used the formatted json version of the original dataset [`/ATUC_Artifacts/Translation_model/toxic_json_GPT35.csv`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Translation_model/toxic_json_GPT35.csv) and you need API from openai.   

Now, if you want to use our prepared finetuned models individually directly and check by giving input and see the generated output, we can use the notebook files named with "All" (e.g., All_T5.ipynb). All the fined-tuned models are shared in [`here`](https://doi.org/10.5281/zenodo.10775868). Please go "Prepared_models" => "Translation Model" => "My fine-tuned translation models." You can find seven fine-tuned models. However, we provided a single script used for all models. Please see  [`/ATUC_Artifacts/colab.md`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/colab.md). Additionally, you can use our finetuned GPT3.5 model to convert uncivil comments into civil counterparts. The model name is ft:gpt-3.5-turbo-0613:software-research-lab:ctbot:814tfHj0. Just give an uncivil comments as prompt and see the generated civil alternatives.   

#### Comparative analysis:
To compare our prepared incivility detection and translation models with existing politeness transfer and detoxification models, we replicated all the state-of-the-arts. Please have a look at the paper for details. We also shared the scripts and replicated models [`here`](https://doi.org/10.5281/zenodo.10775868). For detection models, go "Prepared_models" => "Detection Models" => "General Toxicity detection models" and "Prepared_models" => "Detection Models" => "Politeness Detection models." For translation models, go "Prepared_models" => "Translation Model" => "Detoxification models" and "Prepared_models" => "Translation Model" => "Politeness transfer models." 

For comparison, we used several metrics. All the metrics' descriptions are in the [`/ATUC_Artifacts/Suplementary document.pdf`](https://github.com/Oyakiolo052/ATUC_Artifacts/blob/main/Suplementary document.pdf). All the scripts and results are available in [`/ATUC_Artifacts/Comparative_analysis`](https://github.com/Oyakiolo052/ATUC_Artifacts/tree/main/Comparative_analysis). 






