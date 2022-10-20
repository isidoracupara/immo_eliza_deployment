import pickle
from typing import List
import numpy as np

def predict_price(model_input: List[int]):

    pickle_filename = "model/pickle_model.pkl"
    with open(pickle_filename,'rb') as file:
        pickle_model = pickle.load(file)
    y_pred = pickle_model.predict(np.array(model_input).reshape(-1,1))

    return y_pred
