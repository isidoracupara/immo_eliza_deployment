from typing import Optional
import json
import pandas as pd
import requests
from fastapi import FastAPI, HTTPException

# format of input data:
# {
# "data": {
#     "area": int,
#     "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
#     "rooms-number": int,
#     "zip-code": int,
#     "land-area": Optional[int],
#     "garden": Optional[bool],
#     "garden-area": Optional[int],
#     "equipped-kitchen": Optional[bool],
#     "full-address": Optional[str],
#     "swimming-pool": Optional[bool],
#     "furnished": Optional[bool],
#     "open-fire": Optional[bool],
#     "terrace": Optional[bool],
#     "terrace-area": Optional[int],
#     "facades-number": Optional[int],
#     "building-state": Optional [str] (
#     "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
#     )
# }

def preprocess(data_json):
    #parse json
    data = json.loads(data_json)

    data['garden'] = data['garden'].astype(int)
    data['equipped_kitchen'] = data['equipped_kitchen'].astype(int)
    data['swimming_pool'] = data['swimming_pool'].astype(int)
    data['furnished'] = data['swimming_pool'].astype(int)
    data['open_fire'] = data['open_fire'].astype(int)
    data['terrace'] = data['terrace'].astype(int)


    data['property_type'] = data['property_type'].upper()
    match data["building_state"]:
        case "APARTMENT":
            data['building_state'] = 4
        case "HOUSE":
            data['building_state'] = 2
        case "OTHERS":


    data['building_state'] = data['building_state'].upper()
    match data["building_state"]:
        case "NEW":
            data['building_state'] = 4
        case "GOOD":
            data['building_state'] = 2
        case "TO RENOVATE":
            data['building_state'] = 1
        case "JUST RENOVATED":
            data['building_state'] = 3
        case "TO REBUILD":  
            data['building_state'] = 0

#get this from the cleaning file
    data['zip_code'] = data['zip_code']

    mandatory_data = [data['area'], data['property_type'], data['rooms_number'], data['zip_code']]
    for column in mandatory_data:
        if column == None:
            raise HTTPException(status_code=400, detail="Invalid input. Please include at least area, property type, number of rooms and zip code.")



    return data