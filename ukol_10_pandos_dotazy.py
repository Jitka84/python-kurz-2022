import pandas
import pytemperature


teploty = pandas.read_csv("temperature.txt")

print(teploty.info())

#dotaz na mereni v Praze
print(teploty[teploty["City"] == "Prague"])

#dotaz na avg teplotu > 80
print(teploty[teploty["AvgTemperature"] > 80])

#dotaz na avg teplotu > 60 a Evrpu
print(teploty[(teploty["AvgTemperature"] > 60) & (teploty["Region"] == "Europe" )])

#dotaz rozmezi prumernych teplot
print(teploty[(teploty["AvgTemperature"] > 60) | (teploty["AvgTemperature"] < -20 )])

#BONUS - pridani sloupce v celsia
teploty["AvgTemperatureCelsia"] = pytemperature.f2c(teploty["AvgTemperature"])

#dotaz na avg teplotu > 30
print(teploty[teploty["AvgTemperatureCelsia"] > 30])

#dotaz na avg teplotu > 15 a Evropu
print(teploty[(teploty["AvgTemperatureCelsia"] > 15) & (teploty["Region"] == "Europe" )])

#dotaz rozmezi prumernych teplot   - problem - nevalidni data pro nektere staty 
print(teploty[(teploty["AvgTemperatureCelsia"] > 30) | (teploty["AvgTemperatureCelsia"] < -10 )])

#invalid data pro nektere staty, kde nebylo mereni dostupne - bylo vlozeno -99F
print(teploty[(teploty["AvgTemperature"] == -99)])
