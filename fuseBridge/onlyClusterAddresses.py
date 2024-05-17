import pandas as pd
import os

# List of input CSV files
input_files = [
    'data2/arb_Clusters.csv',
    'data2/bsc_Clusters.csv',
    'data2/eth_Clusters.csv',
    'data2/fuse_Clusters.csv',
    'data2/gnosis_Clusters.csv',
    'data2/matic_Clusters.csv',
    'data2/op_Clusters.csv'
    # Add more file paths as needed
]

# Output file path
output_file = 'data2/onlyClusterAddresses.csv'

# Create the output directory if it does not exist
os.makedirs('data2', exist_ok=True)

# Initialize an empty DataFrame to collect the results
result_df = pd.DataFrame(columns=['SENDER_WALLET'])

# Process each input file
for file in input_files:
    # Read the CSV file
    df = pd.read_csv(file)
    
    # Filter rows where Cluster_Label is not -1
    filtered_df = df[df['Cluster_Label'] != -1]
    
    # Append the SENDER_WALLET column to the result DataFrame
    result_df = pd.concat([result_df, filtered_df[['SENDER_WALLET']]], ignore_index=True)

# Save the result to the output file
result_df.to_csv(output_file, index=False)

print(f"Output saved to {output_file}")
