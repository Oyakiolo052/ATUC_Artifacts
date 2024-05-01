import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load data from CSV
df = pd.read_csv('/u1/mdr614/ATUC_Final/Conversion_uncivil_to_civil_random_2000/Incivility_conversion_results/civilAlternatives_by_Diffudetox_random2000.csv')  # Replace with your CSV file path
sentences_uncivil = df['uncivil'].tolist()
sentences_civil = df['civil'].tolist()

# Define models
models = [
    SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2'),
    SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L12-v2'),
    SentenceTransformer('sentence-transformers/multi-qa-MiniLM-L6-cos-v1'),
    SentenceTransformer('sentence-transformers/nli-mpnet-base-v2'),
    SentenceTransformer('sentence-transformers/all-mpnet-base-v2'),
    SentenceTransformer('bert-base-nli-mean-tokens')
]

# Create a DataFrame to store results
results_df = pd.DataFrame(columns=['Sentence_Uncivil', 'Sentence_Civil', 'Final_Similarity_Score'])

# Iterate over sentences
cnt=0
for uncivil, civil in zip(sentences_uncivil, sentences_civil):
    cnt+=1
    print("Row: ",cnt)
    similarity_scores = []

    # Iterate over models
    for model in models:
        # Compute embeddings
        embedding_uncivil = model.encode(uncivil, convert_to_tensor=True)
        embedding_civil = model.encode(civil, convert_to_tensor=True)

        # Calculate similarity score
        similarity_score_tensor = util.pytorch_cos_sim(embedding_uncivil, embedding_civil)
        similarity_score = similarity_score_tensor.item()

        # Store similarity score
        similarity_scores.append(similarity_score)

    # Find the maximum similarity score among different models
    print(similarity_scores)
    final_sim = max(similarity_scores)


    # Store results in DataFrame
    results_df = results_df.append({
        'Sentence_Uncivil': uncivil,
        'Sentence_Civil': civil,
        'Final_Similarity_Score': final_sim
    }, ignore_index=True)
    

# Calculate average final score
average_final_score = results_df['Final_Similarity_Score'].mean()   #we did not consider the similarity scores where our model failed to generate civil alternatives because they are almost identical.  

# Print results and average final score
#print("Results:")
#print(results_df)
print("\nAverage Final Score:", average_final_score)

# Save results to a CSV file (append mode)
results_df.to_csv('/u1/mdr614/ATUC_Final/Conversion_uncivil_to_civil_random_2000/Incivility_conversion_results/civilAlternatives_by_Diffudetox_random2000_SSim.csv',header=not results_df.index.empty)
