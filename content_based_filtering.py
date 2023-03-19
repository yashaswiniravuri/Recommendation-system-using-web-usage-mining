import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import random

# Load the web usage mining data from the CSV file
data = pd.read_csv('web_usage_mining_data.csv')
users = ['user1', 'user2', 'user3', 'user4', 'user5']

# Compute the pairwise cosine similarities between the products based on their features
product_features = data[['product_id', 'feature1', 'feature2', 'feature3', 'feature4', 'feature5']]
product_features.set_index('product_id', inplace=True)
product_similarity = cosine_similarity(product_features)

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


import pandas as pd
import plotly.graph_objs as go
from sklearn.metrics.pairwise import cosine_similarity

# Load the web usage mining data from the CSV file
data = pd.read_csv('web_usage_mining_data.csv')

# Compute the pairwise cosine similarities between the products based on their features
product_features = data[['product_id', 'feature1', 'feature2', 'feature3', 'feature4', 'feature5']]
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

'''
This will display an interactive heatmap of the cosine similarity matrix, 
where the color of each cell represents the similarity between the corresponding pair of products. 
The darker the color, the higher the similarity. 
The product IDs are shown on both the x-axis and y-axis, 
and the title of the plot indicates that it's a cosine similarity matrix.
'''