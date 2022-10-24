import pickle
from typing import List
import numpy as np

def predict_price(model_input: List[int]) -> dict:
    with open("model/model.pkl",'rb') as file:
        model = pickle.load(file)

    with open("model/poly.pkl", "rb") as poly_file:
        poly_feat = pickle.load(poly_file)

    with open("model/scaler.pkl", "rb") as file_scaler:
        scaler = pickle.load(file_scaler)

    input_array = np.array([model_input])
    X_scaled_input = scaler.transform(input_array)
    prediction = model.predict(poly_feat.fit_transform(X_scaled_input))
    # print(prediction[0])
    return {"prediction": prediction[0]}
