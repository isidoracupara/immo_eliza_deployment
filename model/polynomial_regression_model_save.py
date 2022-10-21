import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, KFold, train_test_split
from sklearn.preprocessing import StandardScaler
pickle_filename = "model/pickle_model.pkl"

df_2 = pd.read_csv('model/data_for_model/postcode_added_data.csv')
X_2 = df_2.drop('price',axis=1).values
y_2 = df_2['price'].values

X_train, X_test, y_train, y_test = train_test_split(X_2, y_2, test_size=0.3, random_state=0)

# print(df_2.head())
# print(X_2.shape)
# print(y_2.shape)
# print(X_2)


scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

with open("model/scaler.pkl", "wb") as file_scaler:
    pickle.dump(scaler, file_scaler)

kf = KFold(n_splits=3, shuffle=True, random_state=42)

#scalar = Scalar
poly = PolynomialFeatures(degree=2)

X_train_poly = poly.fit_transform(X_train)
with open("model/poly.pkl", "wb") as file_poly:
    pickle.dump(poly, file_poly)


reg = LinearRegression()
reg.fit(X_train_poly, y_train)
Y_train_predict = reg.predict(X_train_poly)

with open ("model/model.pkl", 'wb') as file_model:
    pickle.dump(reg, file_model)

rmse_train = np.sqrt(mean_squared_error(y_train, Y_train_predict))
r2_train = r2_score(y_train, Y_train_predict)

print(f"RMSE: {rmse_train}")
print(f"R2: {r2_train}")
# cv_results = cross_val_score(reg, X_pol, y_2, cv=kf)

# print(cv_results,np.mean(cv_results))