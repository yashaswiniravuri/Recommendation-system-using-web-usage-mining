import csv
import random

# Define lists of users, products, and categories
users = ['user1', 'user2', 'user3', 'user4', 'user5']
products = ['product1', 'product2', 'product3', 'product4', 'product5']
categories = ['category1', 'category2', 'category3', 'category4', 'category5']

# Define a function to generate random features for products
def generate_features():
    feature1 = random.uniform(0, 1)
    feature2 = random.uniform(0, 1)
    feature3 = random.uniform(0, 1)
    feature4 = random.uniform(0, 1)
    feature5 = random.uniform(0, 1)
    return [feature1, feature2, feature3, feature4, feature5]

# Generate web usage mining data
data = []
for i in range(1000):
    user_id = random.choice(users)
    product_id = random.choice(products)
    category = random.choice(categories)
    features = generate_features()
    data.append({'user_id': user_id, 'product_id': product_id, 'category': category, 'features': features})

# Write the data to a CSV file
with open('web_usage_mining_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['user_id', 'product_id', 'category', 'feature1', 'feature2', 'feature3', 'feature4', 'feature5']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for entry in data:
        row = {'user_id': entry['user_id'], 'product_id': entry['product_id'], 'category': entry['category']}
        for i, feature in enumerate(entry['features']):
            row[f'feature{i+1}'] = feature
        writer.writerow(row)

import pandas as pd
# Load the web usage data into a Pandas dataframe
df = pd.read_csv('web_usage_mining_data.csv')
# Group the data by user and product
grouped_data = df.groupby(['user_id', 'product_id']).sum()
# Calculate the number of unique users and products
num_users = len(grouped_data.index.get_level_values(0).unique())
num_products = len(grouped_data.index.get_level_values(1).unique())

# Calculate the total number of interactions (page views, purchases, etc.)
total_interactions = grouped_data.sum()[0]

# Calculate the average number of interactions per user and product
avg_interactions_per_user = total_interactions / num_users
avg_interactions_per_product = total_interactions / num_products

# Print the results
print("Number of unique users: ", num_users)
print("Number of unique products: ", num_products)
print("Total number of interactions: ", total_interactions)
print("Average number of interactions per user: ", avg_interactions_per_user)
print("Average number of interactions per product: ", avg_interactions_per_product)
