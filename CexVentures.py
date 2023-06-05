import pandas as pd

# Read BinanceVentures.csv from the Binance folder
binance_df = pd.read_csv('Binance/MergedBinanceVentures.csv')

# Read CoinbaseVentures.csv from the Coinbase folder
coinbase_df = pd.read_csv('Coinbase/CoinbaseVentures.csv')

# Read DCGVentures.csv from the Coinbase folder
dcg_df = pd.read_csv('DCG/DCGVentures.csv')

# Read DCGVentures.csv from the Coinbase folder
a16z_df = pd.read_csv('a16z/Mergeda16zVentures.csv')

# Combine the DataFrames
combined_df = pd.concat([binance_df, coinbase_df, dcg_df, a16z_df], ignore_index=True)

# Export the combined DataFrame to a CSV file named CexVentures.csv
combined_df.to_csv('CexVentures.csv', index=False)

print("CSV file exported successfully!")
