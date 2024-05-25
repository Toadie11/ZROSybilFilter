import pandas as pd

# Specify the path to your CSV file
input_file = "data4/aptosBridgeAddtx.csv"  # Change this to your actual file path
output_file = "results/aptosBridgeTxRemoveDuplicates.csv"

# Read the CSV file
df = pd.read_csv(input_file)

# Filter rows where 'Txs' is 50 or higher
df_filtered = df[df['Txs'] >= 50]

# Drop duplicates based on 'SENDER_WALLET' while keeping the first occurrence
df_cleaned = df_filtered.drop_duplicates(subset='SENDER_WALLET', keep='first')

# Keep only the 'SENDER_WALLET' column
df_final = df_cleaned[['SENDER_WALLET']]

# Write the cleaned DataFrame to a new CSV file
df_final.to_csv(output_file, index=False)

# Print the cleaned DataFrame
print(df_final)

