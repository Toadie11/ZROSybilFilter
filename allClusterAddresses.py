import pandas as pd
import os

# List of input CSV files
input_files = [
    'angle/results/countClusterAddresses.csv',  # replace with your actual file paths
    'aptosBridge/results/countClusterAddresses.csv',
    'btcb/results/countClusterAddresses.csv',
    'core/results/countClusterAddresses.csv',
    'fuseBridge/results/countClusterAddresses.csv',
    'harmony/results/countClusterAddresses.csv',
    'kingdom/results/countClusterAddresses.csv',
    'l2pass/results/countClusterAddresses.csv',
    'l2telegraph/results/countClusterAddresses.csv',
    'merkly/results/countClusterAddresses.csv',
    'gaszip/results/countClusterAddresses.csv'
    # Add more file paths as needed
]

# Output file path
output_file = 'merged_wallet_counts.csv'

# Initialize an empty DataFrame to collect the results
merged_df = pd.DataFrame()

# Process each input file
for file in input_files:
    # Read the CSV file
    df = pd.read_csv(file)
    
    # Group by SENDER_WALLET and sum the counts
    df_grouped = df.groupby('SENDER_WALLET', as_index=False)['count'].sum()
    
    # Append the grouped DataFrame to the merged DataFrame
    merged_df = pd.concat([merged_df, df_grouped], ignore_index=True)

# Group the merged DataFrame by SENDER_WALLET and sum the counts
final_df = merged_df.groupby('SENDER_WALLET', as_index=False)['count'].sum()

# Sort the final DataFrame by count in descending order
final_df = final_df.sort_values(by='count', ascending=False)

# Save the final DataFrame to the output file
final_df.to_csv(output_file, index=False)

print(f"Merged data saved to {output_file}")
