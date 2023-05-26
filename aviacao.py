import pandas as pd

dt = pd.read_csv("ocorrencia.csv", sep=";")
dt_resumido = dt.iloc[: , 3:10]
dt_resumido.sort_values(by="Classificacao_da_Ocorrencia",inplace=True)
dt_Classificacao_da_Ocorrencia= dt_resumido["Classificacao_da_Ocorrencia"]=="Acidente"
print(dt_resumido)
print(dt_resumido[dt_Classificacao_da_Ocorrencia])

