import os
import pandas as pd

def process_chain_data(chain):
    # Read the first CSV file
    df1 = pd.read_csv(f'data3/{chain}_cluster.csv')

    # Read the second CSV file
    df2 = pd.read_csv('../initialList.csv')

    # Ensure columns are correctly named
    assert 'SENDER_WALLET' in df1.columns, f"{chain} CSV does not have column 'SENDER_WALLET'"
    assert 'ADDRESS' in df2.columns, "Second CSV does not have column 'ADDRESS'"

    # Create a set of addresses from the second CSV file
    address_set = set(df2['ADDRESS'])

    # Filter out rows from the first DataFrame where SENDER_WALLET is in the address set
    filtered_df1 = df1[~df1['SENDER_WALLET'].isin(address_set)]

    # Remove duplicates based on SENDER_WALLET
    filtered_df1 = filtered_df1.drop_duplicates(subset='SENDER_WALLET')

    # Save the filtered DataFrame to a new CSV file
    filtered_df1.to_csv(f'data4/{chain}_filtered_list.csv', index=False)

    print(f"Filtered CSV file for {chain} created successfully.")

    # Count occurrences of each Cluster_Label
    cluster_label_counts = filtered_df1['Cluster_Label'].value_counts()

    # Find Cluster_Labels with less than 5 occurrences
    labels_to_remove = cluster_label_counts[cluster_label_counts < 5].index

    # Remove rows with Cluster_Labels having less than 5 occurrences
    filtered_df1 = filtered_df1[~filtered_df1['Cluster_Label'].isin(labels_to_remove)]

    # Save the updated DataFrame to the same CSV file
    filtered_df1.to_csv(f'data4/{chain}_filtered_list.csv', index=False)

    # Create a DataFrame with only the unique SENDER_WALLET values
    unique_senders = filtered_df1[['SENDER_WALLET']].drop_duplicates()

    # Save the unique SENDER_WALLET values to a new CSV file
    with open(f'data4/{chain}_unique_senders.csv', 'w') as f:
        f.write('SENDER_WALLET\n')  # Write the column header
        previous_cluster_label = None
        for index, row in unique_senders.iterrows():
            cluster_label = filtered_df1.loc[filtered_df1['SENDER_WALLET'] == row['SENDER_WALLET'], 'Cluster_Label'].iloc[0]
            if cluster_label != previous_cluster_label:
                if previous_cluster_label is not None:
                    f.write('\n')  # Add a line break if it's a new cluster
                f.write(f"{row['SENDER_WALLET']}\n")
                previous_cluster_label = cluster_label
            else:
                f.write(f"{row['SENDER_WALLET']}\n")

    print(f"CSV file with unique SENDER_WALLET values for {chain} created successfully.")

    print(f"Filtered CSV file for {chain} updated based on Cluster_Label counts.")

# List all files in the 'data3' directory
files = os.listdir('data3')

# Iterate over each file and process the data
for file in files:
    if file.endswith('_cluster.csv'):
        chain = file.split('_')[0]
        process_chain_data(chain)
