import pandas as pd
import statistics

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
print("Informatii privind setul de date")
print(data.info())

print("Media virstei complexelor:")
print(statistics.mean(data.complexAge))
print("Media numarului total de camere:")
print(statistics.mean(data.totalRooms))
print("Media numarului total de camere de baie:")
print(statistics.mean(data.totalBedrooms))
print("Media numarului de locuitori:")
print(statistics.mean(data.complexInhabitants))
print("Media numarului de apartamente in bloc:")
print(statistics.mean(data.apartmentsNr))
print("Meida valoare complexă:")
print(statistics.mean(data.medianComplexValue))
