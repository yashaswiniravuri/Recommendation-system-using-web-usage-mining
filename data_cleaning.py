import pandas as pd
# Load the web usage mining data from the CSV file
df = pd.read_csv('web_usage_data.csv')
# Convert the 'Timestamp' column to a datetime object
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
# Drop any rows with missing values
df.dropna(inplace=True)
# Remove any rows where the 'Action' column is not 'view' or 'add to cart'
df = df[df['Action'].isin(['view', 'add to cart','purchase'])]
# Remove any rows where the 'Action' column is not 'view' or 'add to cart'
df = df[df['Action'].isin(['view', 'add to cart','purchase'])]
# Group the data by user ID and product ID, and count the number of views and adds to cart
df_grouped = df.groupby(['User ID', 'Product ID', 'Action'])['Timestamp'].count().reset_index()
df_grouped.rename(columns={'Timestamp': 'Count'}, inplace=True)
# Keep only the rows with at least 1 view and 1 add to cart
#df_filtered = df_grouped.groupby(['User ID', 'Product ID']).filter(lambda x: len(x) > 1)
# Sort the data by user ID, product ID, and count in descending order
df_sorted = df_grouped.sort_values(by=['User ID', 'Product ID', 'Count'], ascending=[True, True, False])
# Keep only the top 350 rows of the sorted data
df_final = df_sorted.head(350)
# Save the cleaned and preprocessed data to a new CSV file
df_final.to_csv('web_usage_data_cleaned.csv', index=False)