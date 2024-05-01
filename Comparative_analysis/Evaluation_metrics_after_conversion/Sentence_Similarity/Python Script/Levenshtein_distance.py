#!pip install python-Levenshtein

import pandas as pd
import Levenshtein

# Read the CSV file into a DataFrame
df = pd.read_csv('/u1/mdr614/ATUC_Final/Conversion_uncivil_to_civil_random_2000/Incivility_conversion_results/civilAlternatives_by_Diffudetox_random2000.csv')
# Function to calculate Levenshtein Distance similarity
def calculate_similarity(row):
    edit_distance = Levenshtein.distance(row['uncivil'], row['civil'])
    similarity = 1 - (edit_distance / max(len(row['uncivil']), len(row['civil'])))
    return similarity

# Apply the function to create a new column "Sentence_similarity"
df['Sentence_similarity'] = df.apply(calculate_similarity, axis=1)

# Calculate the average similarity
avg_similarity = df['Sentence_similarity'].mean()

# Save the modified DataFrame to a new CSV file
df.to_csv('/u1/mdr614/ATUC_Final/Conversion_uncivil_to_civil_random_2000/Incivility_conversion_results/civilAlternatives_by_Diffudetox_random2000_LD.csv', index=False)

print(f"Results have been saved to your_output_file.csv")
print(f"Average Sentence Similarity: {avg_similarity}")
