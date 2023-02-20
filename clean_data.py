import pandas as pd

our_data = pd.read_csv("Kuala_Lumpur_house_prices.csv")
our_data = our_data.drop("id", axis=1)
print(our_data.info())

our_data['current_price'] = our_data['current_price'].str.replace(',', '').astype(float)
pd.options.display.float_format = '{:.2f}'.format
# print(our_data.describe())
# print(our_data.info())
our_data = our_data.dropna()
our_data.to_csv("Kuala_Lumpur_house_prices_clean.csv", index=False)
our_data = our_data.isna().sum()
our_data = pd.DataFrame(our_data, columns=["null values"])
print(our_data)


