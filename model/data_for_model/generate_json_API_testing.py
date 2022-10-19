from random import randint
import pandas as pd

df = pd.read_csv (r'model/data_for_model/postcode_added_data.csv')


# taking random row 
df = df.iloc[randint(1, len(df. axes[0]))]


df.to_json (r'model/data_for_model/API_test_data.json')