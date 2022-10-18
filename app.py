
# - / -> Just return Alive! if the API is running
#     - GET /predict return a string with the schema of the input expected. That's just for documentation purpose. (Yes FastAPI is already generating a nice documentation, it's just for the exercice)
#     - POST /predict that takes the property details as input and return the prediction as output
from preprocessing.cleaning_data import preprocess
from predict.prediction import predict
from fastapi import FastAPI, status

app = FastAPI()

@app.get("/")
async def root():
    return "Alive"


# {
# "prediction": Optional[float],
# "status_code": Optional[int]
# }

@app.post("/predict")
async def predict_post(new_property_data):
    preprocessed_data = preprocess(new_property_data)
    prediction = predict(preprocessed_data)

    return {'prediction': prediction, 'status_code':status.HTTP_202_ACCEPTED}

@app.get("/predict")
async def predict_get():
    return ('Expected format:\
{"data":\
{"area": int,\
"property-type": "APARTMENT" | "HOUSE" | "OTHERS",\
"rooms-number": int,\
"zip-code": int,\
"land-area": Optional[int],\
"garden": Optional[bool],\
"garden-area": Optional[int],\
"equipped-kitchen": Optional[bool],\
"full-address": Optional[str],\
"swimming-pool": Optional[bool],\
"furnished": Optional[bool],\
"open-fire": Optional[bool],\
"terrace": Optional[bool],\
"terrace-area": Optional[int],\
"facades-number": Optional[int],\
"building-state": Optional [str] \
("NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD") }")')


# class predict(new_property):
#     def get(self):
#         processed_data = preprocess(new_property)
#         prediction = predict(processed_data)
#         return prediction

#     def post(input):

#     api.add_resource(Users, '/users')  # '/users' is our entry point for Users
#     api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations


#     if __name__ == '__main__':
#         app.run()



# class Locations(Resource):
#     # methods go here
#     pass
    


# # push the data through process
# # This wll clean the data so you use the data that is relevant for your specific model
# preprocessed_data = preprocess(data)

# # Then we pass the cleaned data through the model
# prediction = model.predict(preprocessed_data)

# # After that we get prediction results
# # We return the prediction results via a response to the request we got through our API
# return prediction
