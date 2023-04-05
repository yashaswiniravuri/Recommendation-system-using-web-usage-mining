import pandas as pd
import numpy as np
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import accuracy
import plotly.graph_objs as go

# Load data from CSV file
data = pd.read_csv('cleaned_web_usage_data.csv')

# Convert data to Surprise format
reader = Reader(rating_scale=(0, 1), line_format='user item rating', sep=',', skip_lines=1)
data = Dataset.load_from_df(data[['user_id', 'product_id', 'action']], reader)

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

# Convert Surprise data back to Pandas DataFrame
trainset_df = pd.DataFrame(trainset.all_ratings(), columns=['user_id', 'product_id', 'action'])
testset_df = pd.DataFrame(testset, columns=['user_id', 'product_id', 'action'])
data_df = pd.concat([trainset_df, testset_df], ignore_index=True)

# Create user-item rating matrix
ratings_matrix = pd.pivot_table(data_df, values='action', index='user_id', columns='product_id', fill_value=0)

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
