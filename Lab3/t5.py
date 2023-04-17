import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score as r2
from sklearn.metrics import explained_variance_score as evs

# Load data into pandas DataFrame
data = pd.read_csv(
    "/home/ivan/Desktop/ArtificialIntelligence/Lab3/apartmentComplexData.txt",
    header=None,
    usecols=[2, 3, 4, 5, 6, 8],
    names=[
        "complexAge",
        "totalRooms",
        "totalBedrooms",
        "complexInhabitants",
        "apartmentsNr",
        "medianComplexValue",
    ],
)

X = data.drop("medianComplexValue", axis=1)
Y = data["medianComplexValue"]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.5, random_state=0)

ols = LinearRegression()
ols.fit(X_train, y_train)
ols_yhat = ols.predict(X_test)

ridge = Ridge(alpha=0.5)
ridge.fit(X_train, y_train)
ridge_yhat = ridge.predict(X_test)

lasso = Lasso(alpha=0.01)
lasso.fit(X_train, y_train)
lasso_yhat = lasso.predict(X_test)

en = ElasticNet(alpha=0.01)
en.fit(X_train, y_train)
en_yhat = en.predict(X_test)

print("Scorul OLS: {}".format(evs(y_test, ols_yhat)))
print("Scorul Ridge: {}".format(evs(y_test, ridge_yhat)))
print("Scorul Lasso: {}".format(evs(y_test, lasso_yhat)))
print("Variatia ElasticNet: {}".format(evs(y_test, en_yhat)))
print("R-pătrat OLS: {} ".format(r2(y_test, ols_yhat)))
print("R-pătrat Ridge: {} ".format(r2(y_test, ridge_yhat)))
print("R-pătrat Lasso: {} ".format(r2(y_test, lasso_yhat)))
print("R-pătrat ElasticNet: {} ".format(r2(y_test, en_yhat)))
