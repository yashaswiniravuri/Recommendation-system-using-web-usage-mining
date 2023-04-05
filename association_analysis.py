from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd
import plotly.graph_objects as go

# Load the web usage data into a Pandas dataframe
df = pd.read_csv('cleaned_web_usage_data.csv')

# Pivot the data into a binary matrix
pivot_table = df.pivot_table(index='user_id', columns='product_id', values='action', fill_value=0).astype(bool)

# Find frequent itemsets using Apriori algorithm
frequent_itemsets = apriori(pivot_table, min_support=0.04, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1)

# Print the support, confidence, and lift for each rule
for index, row in rules.iterrows():
    print("Rule:", row['antecedents'], "->", row['consequents'])
    print("Support:", row['support'])
    print("Confidence:", row['confidence'])
    print("Lift:", row['lift'])
    print("=====================================")

# Calculate the overall performance metrics for all rules
avg_support = rules['support'].mean()
avg_confidence = rules['confidence'].mean()
avg_lift = rules['lift'].mean()

print("Overall performance metrics:")
print("Average support:", avg_support)
print("Average confidence:", avg_confidence)
print("Average lift:", avg_lift)


# Create the scatter plot
fig = go.Figure(data=go.Scatter(
    x=rules['support'],
    y=rules['confidence'],
    mode='markers',
    marker=dict(
        size=rules['lift'],
        sizemode='diameter',
        sizeref=0.1,
        sizemin=5,
        color=rules['lift'],
        colorscale='rdbu',
        reversescale=True,
        colorbar=dict(
            thickness=15,
            title='Lift',
            xanchor='left',
            titleside='right'
        ),
        line_width=1
    )
))

# Set the plot title and axis labels
fig.update_layout(
    title='Association Rule Scatter Plot',
    xaxis=dict(
        title='Support',
        ticklen=5,
        zeroline=False,
        gridwidth=2,
    ),
    yaxis=dict(
        title='Confidence',
        ticklen=5,
        gridwidth=2,
    ),
    showlegend=False
)

# Show the plot
fig.show()
