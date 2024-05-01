# import numpy as np

# # Given lists
# list_incivility = [76.71, 71.10, 65.63, 76.58, 89.14, 76.44, 75.58, 76.41, 90.95, 94.90]
# list_semantic = [77.70, 89.31, 92.18, 83.14, 90.34, 98.45, 82.83, 81.25, 86.22, 92.34]
# list_sentence = [39.53, 64.85, 80.05, 46.20, 51.76, 85.89, 46.15, 44.47, 38.40, 62.40]
# list_sentiCR = [56.44, 31.87, 13.38, 47.93, 16.30, 41.36, 48.66, 45.01, 42.89, 51.05]
# list_sentSE = [19.63, 11.46, 0.29, 3.01, 1.58, 1.86, 0.14, 3.72, 43.41, 65.90]
# list_roberta = [30.66, 12.67, 13.90, 25.84, 25.76, 6.05, 27.31, 25.35, 27.47, 46.08]

# #minimization

# list_length = [47.19,1.94,1.37,53.79,33.72,6.33,53.71,55.64,56.45,3.06]

# # Subtract each value from 100 becase as the result is better when it is low. So we reverse it. 
# length = [100 - value for value in list_length]

# #print(length)


# # Combine lists into a 2D NumPy array for maximization
# data = np.array([list_incivility, list_semantic, list_sentence, list_sentiCR, list_sentSE, list_roberta,length])

# #print(data)

# # Calculate harmonic mean for each index (column-wise)
# harmonic_means = np.reciprocal(np.mean(np.reciprocal(data), axis=0))

# # Print the results
# for i, mean_value in enumerate(harmonic_means):
#     print(f"Harmonic Mean for Index {i + 1}: {mean_value}")


# print("\n\n")

#join metrics among my proposed model


# Given lists
list_incivility = [94.90,93.92,91.59,79.81,90.09]
list_semantic = [88.98,92.40,90.63,88.09,85.79]
list_sentence = [53.44,62.40,59.08,59.54,41.49]
list_sentiCR = [32.17,21.91,27.97,21.21,51.05]
list_sentSE = [65.04,65.90,50.29,37.39,64.45]
list_roberta = [37.09,32.27,25.57,31.21,39.37]

#minimization

list_length = [11.93,3.06,5.98,15.76,29.98]

# Subtract each value from 100 becase as the result is better when it is low. So we reverse it. 
length = [100 - value for value in list_length]

#print(length)
data = np.array([list_incivility, list_semantic, list_sentence, list_sentiCR, list_sentSE, list_roberta,length])
# Calculate harmonic mean for each index (column-wise)
harmonic_means = np.reciprocal(np.mean(np.reciprocal(data), axis=0))

# Print the results
for i, mean_value in enumerate(harmonic_means):
    print(f"Harmonic Mean for Index {i + 1}: {mean_value}")


