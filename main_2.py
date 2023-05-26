import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("aa.csv",sep=";")
regiao_norte = dataset.loc[:,["Regiao - Sigla","Estado - Sigla","Produto","Valor de Venda"]][dataset["Produto"]== "GASOLINA"][dataset["Regiao - Sigla"]=="N"][dataset["Estado - Sigla"].isin(["AC", "AM"])]
regiao_norte = regiao_norte.sort_values(by="Valor de Venda")

plt.bar(regiao_norte["Estado - Sigla"], regiao_norte["Valor de Venda"])
plt.title("Preço da Gasolina")
plt.xlabel("Estados")
plt.ylabel("Preços")
plt.show()
