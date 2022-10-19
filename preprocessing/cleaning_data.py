from typing import List, Literal, Optional
from fastapi import HTTPException
from pydantic import BaseModel

# map simplifies zip codes into zip code indexes
# from previous project part
def map_postal_code(zip_code: int):
    mapping_zipcode = {73: 1, 64: 2, 60: 3, 76: 4, 71: 5, 56: 6, 79: 7, 55: 8, 41: 9, 61: 10, 44: 11, 62: 12, 70: 13, 65: 14, 48: 15, 40: 16, 45: 17, 68: 18, 77: 19, 43: 20, 50: 21, 95: 22,
        75: 23, 66: 24, 69: 25, 53: 26, 42: 27, 46: 28, 89: 29, 88: 30, 78: 31, 21: 32, 49: 33, 84: 34, 51: 35, 38: 36, 34: 37, 37: 38, 96: 39, 93: 40, 36: 41, 91: 42, 67: 43,
        97: 44, 86: 45, 92: 46, 99: 47, 87: 48, 94: 49, 33: 50, 85: 51, 39: 52, 24: 53, 28: 54, 22: 55, 23: 56, 26: 57, 47: 58, 32: 59, 80: 60, 35: 61, 15: 62, 98: 63, 25: 64,
        17: 65, 14: 66, 82: 67, 10: 68, 18: 69, 90: 70, 20: 71, 13: 72, 31: 73, 16: 74, 12: 75, 29: 76, 30: 77, 11: 78, 83: 79, 19: 80}

    return mapping_zipcode.get(int(zip_code / 100))

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

def preprocess(data: Property) -> List[int]:
    data_dictionary = data.dict()
    processed_data = {}

    # changin collumn names to what my model understands
    # features = ['id', 'locality', 'postal_code', 'region', 'province',
    #    'type_of_property', 'subtype_of_property', 'type_of_sale', 'price',
    #    'number_of_bedrooms', 'surface', 'kitchen_type',
    #    'fully_equipped_kitchen', 'furnished', 'open_fire', 'terrace',
    #    'terrace_surface', 'garden', 'garden_surface', 'land_surface',
    #    'number_of_facades', 'swimming_pool', 'state_of_the_building']

    processed_data['surface'] = data_dictionary['area']
    processed_data['number_of_bedrooms'] = data_dictionary['rooms_number']
    processed_data['land_surface'] = data_dictionary['land_area']
    processed_data['garden_surface'] = data_dictionary['garden_area']
    processed_data['terrace_surface'] = data_dictionary['terrace_area']
    processed_data['number_of_facades'] = data_dictionary['facades_number']    

    # turning bools into int
    processed_data['garden'] = data_dictionary['garden'].astype(int)
    processed_data['fully_equipped_kitchen'] = data_dictionary['equipped_kitchen'].astype(int)
    processed_data['swimming_pool'] = data_dictionary['swimming_pool'].astype(int)
    processed_data['furnished'] = data_dictionary['swimming_pool'].astype(int)
    processed_data['open_fire'] = data_dictionary['open_fire'].astype(int)
    processed_data['terrace'] = data_dictionary['terrace'].astype(int)


    processed_data['type_of_property'] = data_dictionary['property_type']
    match data_dictionary["building_state"]:
        case "APARTMENT":
            data_dictionary['building_state'] = 0
        case "HOUSE":
            data_dictionary['building_state'] = 1


    processed_data['state_of_the_building'] = data_dictionary['building_state']
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

    processed_data['postal_code'] = map_postal_code(data_dictionary['zip_code'])

    # order is important
    # postal_code , type_of_property , number_of_bedrooms, surface, kitchen_type, terrace_surface, land_surface, number_of_facades, swimming_pool, state_of_the_building

    model_input = [
        processed_data['postal_code'],
        processed_data['type_of_property'],
        processed_data['number_of_bedrooms'],
        processed_data['surface'],
        processed_data['kitchen_type'],
        processed_data['terrace_surface'],
        processed_data['land_surface'],
        processed_data['number_of_facades'],
        processed_data['swimming_pool'],
        processed_data['state_of_the_building'],
    ]


    return model_input
