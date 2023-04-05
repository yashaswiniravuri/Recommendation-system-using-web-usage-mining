import pandas as pd
import plotly.graph_objs as go
from sklearn.metrics.pairwise import cosine_similarity
import random

# Load the web usage mining data from the CSV file
data = pd.read_csv('cleaned_web_usage_data.csv')

# Define the list of users
users = data['user_id'].unique()

# Compute the pairwise cosine similarities between the products based on their features# Load the cleaned web usage mining data from the CSV file
data = pd.read_csv('cleaned_web_usage_data.csv')

# Fill in missing values with the mean of each feature
data.fillna(data.mean(), inplace=True)

# Compute the pairwise cosine similarities between the products based on their features
product_features = data[['product_id', 'category', 'price', 'weight', 'feature_type', 'is_brand', 'discount', 'action', 'product_category']]
product_features.set_index('product_id', inplace=True)
product_similarity = cosine_similarity(product_features)

# Create a Plotly heatmap
heatmap = go.Heatmap(
    z=product_similarity,
    x=product_features.index.values,
    y=product_features.index.values,
    colorscale='YlGnBu'
)

# Define layout
layout = go.Layout(
    title='Cosine Similarity Matrix',
    xaxis=dict(title='Product ID'),
    yaxis=dict(title='Product ID')
)

# Create figure object
fig = go.Figure(data=[heatmap], layout=layout)

# Show figure
fig.show()


# Define a function to generate recommendations for a given user
def get_recommendations(user_id, num_recommendations=5):
    # Get the user's purchase history
    user_history = data[data['user_id'] == user_id]['product_id'].unique()
    
    # Compute the average feature vector for the user's purchase history
    user_features = product_features.loc[user_history].mean(axis=0).values.reshape(1, -1)
    
    # Compute the cosine similarities between the user's average feature vector and the product feature vectors
    product_similarity_to_user = cosine_similarity(user_features, product_features)[0]
    
    # Sort the products by similarity to the user and return the top recommendations
    top_indices = product_similarity_to_user.argsort()[::-1][:num_recommendations]
    return product_features.iloc[top_indices].index.values.tolist()

# Test the recommendation model by generating recommendations for a random user
user_id = random.choice(users)
for k in users:
    print(f'Recommendations for user {k}:')
    recommendations = get_recommendations(k)
    for i, product_id in enumerate(recommendations):
        print(f'{i+1}. {product_id}')