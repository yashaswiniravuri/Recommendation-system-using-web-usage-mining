import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv("web_usage_data.csv")
print(data.head())
# Check for missing values
print("Number of missing values in each column:")
print(data.isnull().sum())
data = data.dropna() # drop rows with missing values
# Remove duplicates
#data.drop_duplicates(inplace=True)

# Convert categorical features to numerical
cat_cols = ['user_id', 'product_id', 'category', 'feature3', 'action', 'product_name', 'product_category']
for col in cat_cols:
    data[col] = data[col].astype('category').cat.codes

# Scale numerical features
num_cols = ['feature1', 'feature2', 'feature5']
for col in num_cols:
    data[col] = (data[col] - data[col].min()) / (data[col].max() - data[col].min())

# Rename columns
data.rename(columns={'feature1': 'price', 'feature2': 'weight', 'feature3': 'feature_type', 'feature4': 'is_brand', 'feature5': 'discount'}, inplace=True)

# Drop unnecessary columns
#data.drop(['count', 'rating'], axis=1, inplace=True)

# Save cleaned dataset
data.to_csv('cleaned_web_usage_data.csv', index=False)
