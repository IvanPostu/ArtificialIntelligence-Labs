import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sb  # visualization

# Load data into pandas DataFrame
dataSet = pd.read_csv(
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

plt.subplot(2, 3, 1)
plt.scatter(dataSet["medianComplexValue"], dataSet["complexAge"], color="red")
plt.title("Dependenta dintre pret si virsta")
plt.ylabel("Virsta bloc")
plt.xlabel("Pret in U/M")
plt.subplot(2, 3, 2)
plt.scatter(dataSet["medianComplexValue"], dataSet["totalRooms"], color="blue")
plt.title("Dependenta dintre pret si nr de camere")
plt.ylabel("Nr. de camere")
plt.xlabel("Pret in U/M")
plt.subplot(2, 3, 3)
plt.scatter(dataSet["medianComplexValue"], dataSet["totalBedrooms"], color="orange")
plt.title("Dependenta dintre pret si nr camere sanitare")
plt.ylabel("Nr camere sanitare")
plt.xlabel("Pret in U/M")
plt.subplot(2, 3, 4)
plt.scatter(
    dataSet["medianComplexValue"], dataSet["complexInhabitants"], color="yellow"
)
plt.title("Dependenta dintre pret si nr de locuitori in bloc")
plt.ylabel("Locuitori in bloc")
plt.xlabel("Pret in U/M")
plt.subplot(2, 3, 5)
plt.scatter(dataSet["medianComplexValue"], dataSet["apartmentsNr"], color="green")
plt.title("Dependenta dintre pret si nr de partamente in bloc")
plt.ylabel("Nr apartamente in bloc")
plt.xlabel("Pret in U/M")
plt.subplot(2, 3, 6)
sb.distplot(dataSet["medianComplexValue"], color="maroon")
plt.title("Distributia pretului")
plt.xlabel("Pret in U/M")
plt.subplot(2, 3, 6)
plt.show()
