import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

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
Y = data['medianComplexValue']
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
reg = LinearRegression()
reg.fit(X_train, y_train)

y_pred = reg.predict(X_test)

print("Mean squared error:", mean_squared_error(y_test, y_pred))
print("R^2 score:", r2_score(y_test, y_pred))

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Median Complex Value")
plt.ylabel("Predicted Median Complex Value")
plt.title("Predicted vs Actual Median Complex Value")
plt.show()