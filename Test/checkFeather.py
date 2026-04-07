import pandas as pd

# Load the Feather file
df = pd.read_feather("temperature_data_first10.feather")

# Check the data
print(df)