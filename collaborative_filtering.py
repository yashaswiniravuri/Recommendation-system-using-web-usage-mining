import pandas as pd
import numpy as np
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import accuracy
import plotly.graph_objs as go

# Load data from CSV file
data = pd.read_csv('web_usage_data_cleaned.csv')

# Convert data to Surprise format
reader = Reader(rating_scale=(0, 1), line_format='user item rating', sep=',', skip_lines=1)
data = Dataset.load_from_df(data[['User ID', 'Product ID', 'Count']], reader)

# Split data into train and test sets
trainset, testset = train_test_split(data, test_size=0.2)

# Train the model using Singular Value Decomposition (SVD)
algo = SVD()
algo.fit(trainset)

# Test the model
predictions = algo.test(testset)
# Evaluate model accuracy using Root Mean Squared Error (RMSE)
accuracy.rmse(predictions)
accuracy.mae(predictions)

# Get recommendations for a specific user
user_id = 1
user_items = data.build_full_trainset().ur[user_id]
user_unseen_items = [item for item in algo.trainset.all_items() if item not in user_items]
user_predictions = [algo.predict(user_id, item) for item in user_unseen_items]
top_n_recommendations = sorted(user_predictions, key=lambda x: x.est, reverse=True)[:10]
recommended_items = [pred.iid for pred in top_n_recommendations]
print('Recommended items for user {}: {}'.format(user_id, recommended_items))

data = pd.read_csv('web_usage_data_cleaned.csv')

# Create user-item rating matrix
ratings_matrix = pd.pivot_table(data, values='Count', index='User ID', columns='Product ID', fill_value=0)

# Define Plotly heatmap
heatmap = go.Heatmap(
    z=ratings_matrix.values,
    x=ratings_matrix.columns,
    y=ratings_matrix.index,
    colorscale='YlGnBu'
)

# Define Plotly layout
layout = go.Layout(
    title='User-Item Rating Matrix',
    xaxis=dict(title='Product ID'),
    yaxis=dict(title='User ID')
)

# Create Plotly figure
fig = go.Figure(data=[heatmap], layout=layout)

# Display interactive graph
fig.show()

'''
This will create a heatmap that displays the user-item rating matrix, 
where the x-axis represents the product IDs and the y-axis represents the user IDs. 
The color of each cell indicates the rating value, with darker shades of green indicating higher ratings. 
You can zoom and pan on the graph, and hover over each cell to see the exact rating value.
'''
