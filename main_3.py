import pandas as pd

dt = pd.read_csv("aa.csv", sep=";")
dataset_resumido = dt.iloc[:6,:2]
print(dataset_resumido)