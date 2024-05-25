import pandas as pd

# Read the original CSV file
df_original = pd.read_csv('data/testBridge_txs.csv')

# Calculate the number of transactions for each sender wallet
txs_count = df_original['SENDER_WALLET'].value_counts()

# Map the sender wallet to its transaction count
df_original['Txs'] = df_original['SENDER_WALLET'].map(txs_count)

# Sort the DataFrame by the "Txs" column in descending order
df_sorted = df_original.sort_values(by='Txs', ascending=False)

# Save the sorted DataFrame to a new CSV file
output_file_path = 'data2/testBridgeAddTx.csv'
df_sorted.to_csv(output_file_path, index=False)

# Display a message indicating the file has been saved
print(f"Saved the sorted DataFrame to {output_file_path}")
