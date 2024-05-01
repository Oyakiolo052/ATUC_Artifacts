import pandas as pd
from transformers import AutoTokenizer
import matplotlib.pyplot as plt

# Assuming df is your DataFrame with columns 'uncivil' and 'civil'
df = pd.read_csv('/u1/mdr614/ATUC_Final/Conversion_uncivil_to_civil_random_2000/Incivility_conversion_results/civilAlternatives_by_T5_random2000.csv')  # Replace 'your_file.csv' with the actual CSV file name


# Choose a pre-trained tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Tokenize 'uncivil' and 'civil' columns and calculate token sizes
df['uncivil_tokens'] = df['uncivil'].apply(lambda x: len(tokenizer(x)['input_ids']))
df['civil_tokens'] = df['civil'].apply(lambda x: len(tokenizer(x)['input_ids']))

# Pair and sort based on 'uncivil_tokens'
token_pairs = list(zip(df['uncivil_tokens'], df['civil_tokens']))
sorted_pairs = sorted(token_pairs, key=lambda x: x[0])

# Print the sorted pairs
for uncivil_size, civil_size in sorted_pairs:
    print(f"Uncivil Tokens: {uncivil_size}, Civil Tokens: {civil_size}")

# Create a DataFrame with sorted pairs and row numbers
sorted_df = pd.DataFrame(sorted_pairs, columns=['uncivil_tokens', 'civil_tokens'])
sorted_df['row_number'] = range(1, len(sorted_df) + 1)

# Save the DataFrame to a new CSV file
sorted_df.to_csv('sorted_token_sizes4.csv', index=False)
