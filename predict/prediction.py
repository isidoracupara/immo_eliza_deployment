
    # {
    # "prediction": Optional[float],
    # "status_code": Optional[int]
    # }

import pickle

def predict(data):
    pickle_filename = "pickle_model.pkl"
    with open(pickle_filename,'rb') as file:
        pickle_model = pickle.load(file)
    y_pred = pickle_model.predict(data)

    return y_pred
