import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

# Assuming sorted_df is your DataFrame with sorted token sizes
sorted_df = pd.read_csv('charcter_count_all.csv')  # Replace 'sorted_token_sizes.csv' with the actual CSV file name

# Normalize the 'uncivil' and 'civil' token sizes
scaler = StandardScaler()
sorted_df['uncivil_tokens_normalized'] = scaler.fit_transform(sorted_df[['uncivil_tokens']])
sorted_df['bart_tokens_normalized'] = scaler.fit_transform(sorted_df[['bart']])
sorted_df['CondaBert_tokens_normalized'] = scaler.fit_transform(sorted_df[['condabert']])
sorted_df['GPT4_tokens_normalized'] = scaler.fit_transform(sorted_df[['gpt4']])
sorted_df['GPT35_tokens_normalized'] = scaler.fit_transform(sorted_df[['gpt35']])
sorted_df['madan_tokens_normalized'] = scaler.fit_transform(sorted_df[['madan']])
sorted_df['marco_tokens_normalized'] = scaler.fit_transform(sorted_df[['marco']])
sorted_df['marian_tokens_normalized'] = scaler.fit_transform(sorted_df[['marian']])
sorted_df['nllb_tokens_normalized'] = scaler.fit_transform(sorted_df[['nllb']])
sorted_df['paradetox_tokens_normalized'] = scaler.fit_transform(sorted_df[['paradetox']])
sorted_df['paragedi_tokens_normalized'] = scaler.fit_transform(sorted_df[['paragedi']])
sorted_df['politebot_tokens_normalized'] = scaler.fit_transform(sorted_df[['politebot']])
sorted_df['T5_tokens_normalized'] = scaler.fit_transform(sorted_df[['T5']])
sorted_df['Count_tokens_normalized'] = scaler.fit_transform(sorted_df[['count']])
sorted_df['Diffudetox_tokens_normalized'] = scaler.fit_transform(sorted_df[['diffudetox']])

# Prepare the data
X = sorted_df['row_number'].values.reshape(-1, 1)
y_uncivil = sorted_df['uncivil_tokens_normalized'].values.reshape(-1, 1)
y_bart = sorted_df['bart_tokens_normalized'].values.reshape(-1, 1)
y_condabert = sorted_df['CondaBert_tokens_normalized'].values.reshape(-1, 1)
y_GPT4 = sorted_df['GPT4_tokens_normalized'].values.reshape(-1, 1)
y_GPT35 = sorted_df['GPT35_tokens_normalized'].values.reshape(-1, 1)
y_madan = sorted_df['madan_tokens_normalized'].values.reshape(-1, 1)
y_marco = sorted_df['marco_tokens_normalized'].values.reshape(-1, 1)
y_marian = sorted_df['marian_tokens_normalized'].values.reshape(-1, 1)
y_nllb = sorted_df['nllb_tokens_normalized'].values.reshape(-1, 1)
y_paradetox = sorted_df['paradetox_tokens_normalized'].values.reshape(-1, 1)
y_paragedi = sorted_df['paragedi_tokens_normalized'].values.reshape(-1, 1)
y_politebot = sorted_df['politebot_tokens_normalized'].values.reshape(-1, 1)
y_t5 = sorted_df['T5_tokens_normalized'].values.reshape(-1, 1)
y_count = sorted_df['Count_tokens_normalized'].values.reshape(-1, 1)
y_diffudetox = sorted_df['Diffudetox_tokens_normalized'].values.reshape(-1, 1)



# Fit polynomial regression models
degree = 2
model_uncivil = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_uncivil.fit(X, y_uncivil)

model_bart = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_bart.fit(X, y_bart)

model_condabert = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_condabert.fit(X, y_condabert)

model_GPT4 = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_GPT4.fit(X, y_GPT4)

model_GPT35 = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_GPT35.fit(X, y_GPT35)

model_madan = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_madan.fit(X, y_madan)

model_marco= make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_marco.fit(X, y_marco)

model_marian = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_marian.fit(X, y_marian)

model_nllb = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_nllb.fit(X, y_nllb)

model_paradetox = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_paradetox.fit(X, y_paradetox)

model_paragedi = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_paragedi.fit(X, y_paragedi)

model_politebot = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_politebot.fit(X, y_politebot)

model_t5 = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_t5.fit(X, y_t5)

model_count = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_count.fit(X, y_count)

model_diffudetox= make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_diffudetox.fit(X, y_diffudetox)



# Predict values using the models
X_pred = np.arange(min(X), max(X) + 1).reshape(-1, 1)
y_pred_uncivil = model_uncivil.predict(X_pred)
y_pred_bart = model_bart.predict(X_pred)
y_pred_condabert = model_condabert.predict(X_pred)
y_pred_GPT4 = model_GPT4.predict(X_pred)
y_pred_GPT35 = model_GPT35.predict(X_pred)
y_pred_madan = model_madan.predict(X_pred)
y_pred_marco = model_marco.predict(X_pred)
y_pred_marian = model_marian.predict(X_pred)
y_pred_nllb = model_nllb.predict(X_pred)
y_pred_paradetox = model_paradetox.predict(X_pred)
y_pred_paragedi = model_paragedi.predict(X_pred)
y_pred_politebot = model_politebot.predict(X_pred)
y_pred_t5 = model_t5.predict(X_pred)
y_pred_count = model_count.predict(X_pred)
y_pred_diffudetox = model_diffudetox.predict(X_pred)



# Calculate the mean squared difference between the two lines
mean_squared_difference_T5 = np.mean((y_pred_uncivil - y_pred_t5) ** 2)
mean_squared_difference_Bart = np.mean((y_pred_uncivil - y_pred_bart) ** 2)
mean_squared_difference_nllb = np.mean((y_pred_uncivil - y_pred_nllb) ** 2)
mean_squared_difference_marian = np.mean((y_pred_uncivil - y_pred_marian) ** 2)
mean_squared_difference_GPT35 = np.mean((y_pred_uncivil - y_pred_GPT35) ** 2)
mean_squared_difference_GPT4 = np.mean((y_pred_uncivil - y_pred_GPT4) ** 2)
mean_squared_difference_politebot = np.mean((y_pred_uncivil - y_pred_politebot) ** 2)
mean_squared_difference_madan = np.mean((y_pred_uncivil - y_pred_madan) ** 2)
mean_squared_difference_marco = np.mean((y_pred_uncivil - y_pred_marco) ** 2)
mean_squared_difference_paradetox = np.mean((y_pred_uncivil - y_pred_paradetox) ** 2)
mean_squared_difference_paragedi = np.mean((y_pred_uncivil - y_pred_paragedi) ** 2)
mean_squared_difference_condabert = np.mean((y_pred_uncivil - y_pred_condabert) ** 2)
mean_squared_difference_count = np.mean((y_pred_uncivil - y_pred_count) ** 2)
mean_squared_difference_diffudetox = np.mean((y_pred_uncivil - y_pred_diffudetox) ** 2)
# Print the mean squared difference
print("mean_squared_difference_T5: ",mean_squared_difference_T5)
print("mean_squared_difference_Bart: ",mean_squared_difference_Bart)
print("mean_squared_difference_nllb: ",mean_squared_difference_nllb)
print("mean_squared_difference_marian: ",mean_squared_difference_marian)
print("mean_squared_difference_GPT35: ",mean_squared_difference_GPT35)
print("mean_squared_difference_GPT4: ",mean_squared_difference_GPT4)
print("mean_squared_difference_politebot: ",mean_squared_difference_politebot)
print("mean_squared_difference_madan: ",mean_squared_difference_madan)
print("mean_squared_difference_marco: ",mean_squared_difference_marco)
print("mean_squared_difference_paradetox: ",mean_squared_difference_paradetox)
print("mean_squared_difference_paragedi: ",mean_squared_difference_paragedi)
print("mean_squared_difference_condabert: ",mean_squared_difference_condabert)
print("mean_squared_difference_count: ",mean_squared_difference_count)
print("mean_squared_difference_diffudetox: ",mean_squared_difference_diffudetox)


best_myModel = min(mean_squared_difference_T5,mean_squared_difference_Bart,mean_squared_difference_nllb,mean_squared_difference_marian,mean_squared_difference_GPT35)
print("Best: ",best_myModel)

# Visualize the results including the difference
plt.figure(figsize=(10, 6))
plt.plot(X_pred, y_pred_uncivil, label='Original', linestyle=':', linewidth=8, alpha=0.3,color='blue')
plt.plot(X_pred, y_pred_GPT4, label='GPT 4.0', linestyle='-', linewidth=2, alpha=1,color='orange')
plt.plot(X_pred, y_pred_politebot, label='ChatBot', linestyle='-', linewidth=2, alpha=1,color='green')
plt.plot(X_pred, y_pred_madan, label='PoliteTransfer', linestyle='-', linewidth=2, alpha=1,color='red')
plt.plot(X_pred, y_pred_marco, label='Marco', linestyle='-', linewidth=2, alpha=1,color='purple')
plt.plot(X_pred, y_pred_paradetox, label='Paradetox', linestyle='-', linewidth=2, alpha=1,color='brown')
plt.plot(X_pred, y_pred_paragedi, label='ParaGedi', linestyle='-', linewidth=2, alpha=1,color='pink')
plt.plot(X_pred, y_pred_condabert, label='CondaBert', linestyle='-', linewidth=2, alpha=1,color='gray')
plt.plot(X_pred, y_pred_count, label='CondaBert', linestyle='-', linewidth=2, alpha=1,color='magenta')
plt.plot(X_pred, y_pred_diffudetox, label='DiffuDetox', linestyle='-', linewidth=2, alpha=1,color='cyan')






plt.xlabel('Uncivil comment position (sorted based on intial token size)')
plt.ylabel('Normalized Token Sizes')
#plt.title('Polynomial Regression between Uncivil and corresponding Civil counterparts ()')
plt.legend()
plt.grid(True)
plt.savefig('polynomial_regression_comparison1.jpg')
plt.show()







plt.figure(figsize=(10, 6))
plt.plot(X_pred, y_pred_uncivil, label='Original', linestyle=':', linewidth=8, alpha=0.3,color='blue')
plt.plot(X_pred, y_pred_t5, label='T5', linestyle='-', linewidth=2, alpha=0.8)
plt.plot(X_pred, y_pred_bart, label='BART', linestyle='-', linewidth=2, alpha=0.8)
plt.plot(X_pred, y_pred_nllb, label='NLLB', linestyle='-', linewidth=2, alpha=0.8)
plt.plot(X_pred, y_pred_marian, label='MARIANMT', linestyle='-', linewidth=2, alpha=0.8)
plt.plot(X_pred, y_pred_GPT35, label='GPT 3.5', linestyle='-', linewidth=2, alpha=0.8)
#plt.plot(X_pred, y_pred_GPT4, label='GPT 4.0', linestyle='-', linewidth=2, alpha=0.8)
#plt.plot(X_pred, y_pred_politebot, label='ChatBot', linestyle='-', linewidth=2, alpha=0.8)
#plt.plot(X_pred, y_pred_madan, label='PoliteTransfer', linestyle='-', linewidth=2, alpha=0.8)
#plt.plot(X_pred, y_pred_marco, label='Marco', linestyle='-', linewidth=2, alpha=0.8)
#plt.plot(X_pred, y_pred_paradetox, label='Paradetox', linestyle='-', linewidth=2, alpha=0.8)
#plt.plot(X_pred, y_pred_paragedi, label='ParaGedi', linestyle='-', linewidth=2, alpha=0.8)
#plt.plot(X_pred, y_pred_condabert, label='COndaBert', linestyle='-', linewidth=2, alpha=0.8)

plt.xlabel('Uncivil comment position (sorted based on intial token size)')
plt.ylabel('Normalized Token Sizes')
#plt.title('Polynomial Regression between Uncivil and corresponding Civil counterparts')
plt.legend()
plt.grid(True)
plt.savefig('polynomial_regression_comparison2.jpg')
plt.show()




# # Visualize the results side by side
# fig, axes = plt.subplots(1, 2, figsize=(20, 6))

# # First subplot (left side)
# axes[0].plot(X_pred, y_pred_uncivil, label='Original', linestyle='-', linewidth=8, alpha=0.3, color='blue')
# axes[0].plot(X_pred, y_pred_t5, label='T5', linestyle='-', linewidth=2, alpha=0.8)
# axes[0].plot(X_pred, y_pred_bart, label='BART', linestyle='-', linewidth=2, alpha=0.8)
# axes[0].plot(X_pred, y_pred_nllb, label='NLLB', linestyle='-', linewidth=2, alpha=0.8)
# axes[0].plot(X_pred, y_pred_marian, label='MARIANMT', linestyle='-', linewidth=2, alpha=0.8)
# axes[0].plot(X_pred, y_pred_GPT35, label='GPT 3.5', linestyle='-', linewidth=2, alpha=0.8)
# axes[0].set_xlabel('Row Number')
# axes[0].set_ylabel('Normalized Token Sizes')
# axes[0].set_title('Polynomial Regression Comparison between Uncivil and Civil')
# axes[0].legend()
# axes[0].grid(True)

# # Second subplot (right side)
# axes[1].plot(X_pred, y_pred_uncivil, label='Original', linestyle='-', linewidth=8, alpha=0.3, color='blue')
# axes[1].plot(X_pred, y_pred_GPT4, label='GPT 4.0', linestyle='-', linewidth=2, alpha=0.8)
# axes[1].plot(X_pred, y_pred_politebot, label='ChatBot', linestyle='-', linewidth=2, alpha=0.8)
# axes[1].plot(X_pred, y_pred_madan, label='PoliteTransfer', linestyle='-', linewidth=2, alpha=0.8)
# axes[1].plot(X_pred, y_pred_marco, label='Marco', linestyle='-', linewidth=2, alpha=0.8)
# axes[1].plot(X_pred, y_pred_paradetox, label='Paradetox', linestyle='-', linewidth=2, alpha=0.8)
# axes[1].plot(X_pred, y_pred_paragedi, label='ParaGedi', linestyle='-', linewidth=2, alpha=0.8)
# axes[1].plot(X_pred, y_pred_condabert, label='COndaBert', linestyle='-', linewidth=2, alpha=0.8)
# axes[1].set_xlabel('Row Number')
# axes[1].set_ylabel('Absolute Difference')
# axes[1].set_title('Absolute Difference between Uncivil and Civil')
# axes[1].legend()
# axes[1].grid(True)

# plt.show()


# fig, axes = plt.subplots(2, 1, figsize=(10, 12), sharex=True, sharey=True, gridspec_kw={'hspace': 0.2})  # Use sharex=True for a shared x-axis

# fig.subplots_adjust(hspace=0)
# # First subplot (left side)
# axes[0].plot(X_pred, y_pred_uncivil, label='Original', linestyle='-', linewidth=8, alpha=0.3, color='blue')
# axes[0].set_xlabel('Row Number')
# axes[0].set_ylabel('Normalized Token Sizes')
# axes[0].set_title('Polynomial Regression Comparison between Uncivil and Civil')
# axes[0].legend()
# axes[0].grid(True)

# # Second subplot (right side)
# axes[1].plot(X_pred, difference, label='Absolute Difference', linestyle='--', linewidth=2, alpha=0.8, color='green')
# axes[1].set_xlabel('Row Number')
# axes[1].set_ylabel('Absolute Difference')
# axes[1].set_title('Absolute Difference between Uncivil and Civil')
# axes[1].legend()
# axes[1].grid(True)

# plt.show()




