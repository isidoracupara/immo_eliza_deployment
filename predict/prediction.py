import pickle
from typing import List

def predict_price(model_input: List[int])-> float:

    pickle_filename = "model/pickle_model.pkl"
    with open(pickle_filename,'rb') as file:
        pickle_model = pickle.load(file)
    # y_pred = pickle_model.predict(model_input)

    return 0.0 #y_pred
