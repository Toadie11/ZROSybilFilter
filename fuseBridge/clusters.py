import pandas as pd
from sklearn.cluster import DBSCAN

# Read the CSV file
df = pd.read_csv('convertTime/eth_numeric_dates.csv')

# Extract the numeric timestamps
timestamps = df['SOURCE_TIMESTAMP_NUMERIC'].values.reshape(-1, 1)

# Define DBSCAN parameters
eps = 1000  # maximum distance between two samples to be considered as neighbors (300 seconds = 5 minutes)
min_samples = 20  # minimum number of samples in a cluster

# Initialize DBSCAN
dbscan = DBSCAN(eps=eps, min_samples=min_samples)

# Fit DBSCAN to the data
dbscan.fit(timestamps)

# Get cluster labels (-1 represents noise)
labels = dbscan.labels_

# Add cluster labels to the DataFrame
df['Cluster_Label'] = labels

# Sort clusters by cluster label in descending order
sorted_clusters = df.sort_values(by='Cluster_Label', ascending=False)

# Save the sorted DataFrame to a new CSV file
sorted_clusters.to_csv('data2/eth_Clusters.csv', index=False)
