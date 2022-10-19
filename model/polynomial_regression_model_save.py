import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, KFold

pickle_filename = "pickle_model.pkl"

df_2 = pd.read_csv(r'data_for_model\postcode_added_data.csv')
X_2 = df_2.drop('price',axis=1).values
y_2 = df_2['price'].values

kf = KFold(n_splits=3, shuffle=True, random_state=42)

pol = PolynomialFeatures(degree=2)

X_pol = pol.fit_transform(X_2)

reg = LinearRegression()


with open (pickle_filename, 'wb') as file:
    pickle.dump(reg, file)


cv_results = cross_val_score(reg, X_pol, y_2, cv=kf)

print(cv_results,np.mean(cv_results))