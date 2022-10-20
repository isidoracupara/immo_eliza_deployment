from random import randint
import pandas as pd

df = pd.read_csv (r'model/data_for_model/postcode_added_data.csv')

# generates one random property from scraped data
df = df.iloc[randint(1, len(df. axes[0]))]

# saves json file of the single property data 
df.to_json ('model/data_for_model/API_test_data.json')

# this single property data is not cleaned or formatted for the API
# must be manually formatted as shown below

# Expected format for API input:
# {
#     "area": 97,
#     "property_type": "APARTMENT",
#     "rooms_number": 2,
#     "zip_code": 2500,
#     "land_area": 0,
#     "garden": true,
#     "garden_area": 0,
#     "equipped_kitchen": true,
#     "full_address": "t",
#     "swimming_pool": false,
#     "furnished": false,
#     "open_fire": false,
#     "terrace": true,
#     "terrace_area": 11,
#     "facades_number": 0,
#     "building_state": "JUST RENOVATED"
# }