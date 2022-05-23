import pandas

zvirata_adopce = pandas.read_csv("adopce-zvirat.csv", sep=";", header="infer")
#nazvy sloupcu
print(zvirata_adopce.info())

#zvire s indexem 34   - Ibis bílý
print(zvirata_adopce.iloc[34, [1,2]])

#bonus - nastaveni indexu na jmeno zvirete
zvirata_adopce_bonus = pandas.read_csv("adopce-zvirat.csv", sep=";", index_col="nazev_cz")

#overeni unikatnosti indexu
print(zvirata_adopce_bonus.index.is_unique)

#serazeni indexu
zvirata_adopce_sorted = zvirata_adopce_bonus.sort_index()
print(zvirata_adopce_sorted) 

#vyhledani outlone
print(zvirata_adopce_sorted.loc["Outloň váhavý"])

#vypis intervalu
print(zvirata_adopce_sorted.loc["Želva Smithova":"Želva žlutočelá"])


