import pandas as pd

def calculate_normalized_length_change(original_sentence, modified_sentence):
    if modified_sentence == "Not generated":
        modified_sentence = original_sentence

    original_length = len(original_sentence)
    modified_length = len(modified_sentence)

    length_diff = original_length - modified_length
    

    normalized_length_diff = length_diff / original_length

    normalized_length_change_percentage = normalized_length_diff * 100

    if length_diff < 0:
        change_direction = "increase"
    elif length_diff > 0:
        change_direction = "decrease"
    else:
        change_direction = "no change"

    return normalized_length_change_percentage, length_diff, change_direction

# Load your CSV data into a DataFrame (replace 'your_data.csv' with the actual file name)
df = pd.read_csv('/u1/mdr614/ATUC_Final/Conversion_uncivil_to_civil_random_2000/Incivility_conversion_results/civilAlternatives_by_GPT4_random2000.csv')

# Create new columns to store the results
df['normalized_length_change'] = 0.0
df['length_diff'] = 0
df['change_direction'] = ""

# Iterate through the rows and calculate the metrics
for index, row in df.iterrows():
    uncivil_sentence = row['uncivil']
    civil_sentence = row['civil']
    

    percentage_change, length_diff, change_direction = calculate_normalized_length_change(uncivil_sentence, civil_sentence)

    df.at[index, 'normalized_length_change'] = percentage_change
    df.at[index, 'length_diff'] = length_diff
    df.at[index, 'change_direction'] = change_direction

# Calculate the average change
average_change = df['normalized_length_change'].mean()

from scipy.stats import trim_mean

trimmed_mean_uncivil = trim_mean(df['normalized_length_change'], proportiontocut=0.05)

print("Mean':", trimmed_mean_uncivil)






# Determine whether it's an increase or decrease
overall_change_direction = "increase" if average_change < 0 else "decrease" if average_change > 0 else "no change"

# Display the results
#print(f"Average Normalized Length Change: {average_change:.2f}%")
print(f"Overall Change Direction: {overall_change_direction}")

# Save the modified DataFrame to a new CSV file
df.to_csv('GPT4_Politenes_character_length.csv', index=False)

