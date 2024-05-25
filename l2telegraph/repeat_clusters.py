import pandas as pd
from collections import defaultdict

# Step 1: Read the single CSV file
file_path = 'data3/Arbitrum_cluster.csv'
df = pd.read_csv(file_path)

# Step 2: Remove duplicates within each cluster
df = df.drop_duplicates(subset=['Cluster_Label', 'SENDER_WALLET'])

# Step 3: Group by Cluster_Label and aggregate SENDER_WALLET into sets
clusters = df.groupby('Cluster_Label')['SENDER_WALLET'].apply(set).reset_index()

# Step 4: Find clusters that share at least 10 SENDER_WALLET addresses
cluster_matches = defaultdict(list)
processed_clusters = set()

for i in range(len(clusters)):
    for j in range(i + 1, len(clusters)):
        common_wallets = clusters.at[i, 'SENDER_WALLET'] & clusters.at[j, 'SENDER_WALLET']
        if len(common_wallets) >= 10:
            cluster_key = frozenset(common_wallets)
            if (clusters.at[i, 'Cluster_Label'] not in processed_clusters and 
                clusters.at[j, 'Cluster_Label'] not in processed_clusters):
                cluster_matches[cluster_key].append(clusters.at[i, 'Cluster_Label'])
                cluster_matches[cluster_key].append(clusters.at[j, 'Cluster_Label'])
                processed_clusters.add(clusters.at[i, 'Cluster_Label'])
                processed_clusters.add(clusters.at[j, 'Cluster_Label'])

# Step 5: Prepare the result DataFrame
result_data = []
for wallets, cluster_labels in cluster_matches.items():
    result_data.append({
        'SENDER_WALLET': list(wallets),
        'Repeated_Clusters': len(set(cluster_labels)),
        'Cluster_Labels': list(set(cluster_labels))
    })

result_df = pd.DataFrame(result_data)

# Step 6: Sort the DataFrame by Repeated_Clusters in descending order
result_df = result_df.sort_values(by='Repeated_Clusters', ascending=False)

# Step 7: Write the result to a new CSV file
result_df.to_csv('repeated_clusters.csv', index=False, sep='|')

print('Results have been written to repeated_clusters.csv')
