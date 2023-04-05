import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import plotly.graph_objects as go

# Load user behavior data
user_behavior = pd.read_csv('cleaned_web_usage_data.csv')

# Load product data
products = user_behavior[['product_id', 'product_name', 'product_category']].drop_duplicates()

# Create user-item matrix
user_item_matrix = user_behavior.pivot_table(index='user_id', columns='product_id', values='action').fillna(0)

# Calculate cosine similarity matrix
item_similarity = cosine_similarity(user_item_matrix.T)

# Define hybrid filter function
def hybrid_filter(user_id, num_recs=5):
    user_products = user_item_matrix.loc[user_id].to_numpy().reshape(1,-1)
    product_scores = item_similarity.dot(user_products.T).flatten()
    recommended_products_ids = product_scores.argsort()[:-num_recs-1:-1]
    recommended_products = products.loc[products['product_id'].isin(recommended_products_ids)]
    return recommended_products

# Get recommended products for a sample user
recommended_products = hybrid_filter(11)

# Create a scatter plot of recommended products
fig = go.Figure(go.Scatter(
            x=recommended_products['product_name'],
            y=[1]*len(recommended_products),
            text=recommended_products['product_category'],
            mode='markers',
            marker=dict(
                size=100,
                color=[i for i in range(len(recommended_products))],
                colorscale='Viridis',
                showscale=True
            )
            ))
fig.update_layout(title='Recommended Products for User 11', xaxis_title='Product ID', yaxis_title='Similarity Rank')
fig.show()
