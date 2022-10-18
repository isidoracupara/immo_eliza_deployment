from typing import Literal, Optional
import json
from fastapi import HTTPException
from pydantic import BaseModel


class Property(BaseModel):
    area: int
    property_type: Literal["APARTMENT"] | Literal["HOUSE"] | Literal["OTHERS"]
    rooms_number: int
    zip_code: int
    land_area: Optional[int]
    garden: Optional[bool]
    garden_area: Optional[int]
    equipped_kitchen: Optional[bool]
    full_address: Optional[str]
    swimming_pool: Optional[bool]
    furnished: Optional[bool]
    open_fire: Optional[bool]
    terrace: Optional[bool]
    terrace_area: Optional[int]
    facades_number: Optional[int]
    building_state: Optional[
        Literal["NEW"] | Literal["GOOD"] | Literal["TO RENOVATE"] | Literal["JUST RENOVATED"] | Literal["TO REBUILD"]]

def preprocess(data: Property):
    data_dictionary = data.dict()
    data_dictionary['garden'] = data_dictionary['garden'].astype(int)
    data_dictionary['equipped_kitchen'] = data_dictionary['equipped_kitchen'].astype(int)
    data_dictionary['swimming_pool'] = data_dictionary['swimming_pool'].astype(int)
    data_dictionary['furnished'] = data_dictionary['swimming_pool'].astype(int)
    data_dictionary['open_fire'] = data_dictionary['open_fire'].astype(int)
    data_dictionary['terrace'] = data_dictionary['terrace'].astype(int)


    data_dictionary['property_type'] = data_dictionary['property_type'].upper()
    match data_dictionary["building_state"]:
        case "APARTMENT":
            data_dictionary['building_state'] = 4
        case "HOUSE":
            data_dictionary['building_state'] = 2


    data_dictionary['building_state'] = data_dictionary['building_state'].upper()
    match data_dictionary["building_state"]:
        case "NEW":
            data_dictionary['building_state'] = 4
        case "GOOD":
            data_dictionary['building_state'] = 2
        case "TO RENOVATE":
            data_dictionary['building_state'] = 1
        case "JUST RENOVATED":
            data_dictionary['building_state'] = 3
        case "TO REBUILD":  
            data_dictionary['building_state'] = 0


    mandatory_data = [data_dictionary['area'], data_dictionary['property_type'], data_dictionary['rooms_number'], data_dictionary['zip_code']]
    for column in mandatory_data:
        if column == None | column == 0:
            raise HTTPException(status_code=400, detail="Invalid input. Please include at least area, property type, number of rooms and zip code.")

#get this from the cleaning file
    data_dictionary['zip_code'] = data_dictionary['zip_code']


    return data_dictionary