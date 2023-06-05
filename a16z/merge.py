import pandas as pd

# Read the CSV files with specified encoding
descriptions_df = pd.read_csv("Descriptions.csv", encoding="latin1")
binance_ventures_df = pd.read_csv("BinanceVentures.csv", encoding="latin1")

# Create a dictionary mapping links to descriptions
description_dict = descriptions_df.set_index("Link")["Description"].to_dict()

# Update the "Description" column in BinanceVentures.csv based on the links
binance_ventures_df["Description"] = binance_ventures_df["Link"].map(description_dict)

# Save the updated dataframe to a new CSV file
binance_ventures_df.to_csv("MergedBinanceVentures.csv", index=False)
