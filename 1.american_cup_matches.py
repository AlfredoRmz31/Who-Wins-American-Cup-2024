import pandas as pd
from string import ascii_uppercase as alfabeto
import pickle
import numpy as np

#Scrapping data from wiki

yrs = pd.read_html("https://es.wikipedia.org/wiki/Copa_Am%C3%A9rica")
yrs_c = list(yrs.pop("Edición"))
df1 = pd.read_html("https://es.wikipedia.org/wiki/Copa_Am%C3%A9rica_2024")

df1 = pd.read_html("https://es.wikipedia.org/wiki/Copa_Am%C3%A9rica_2024")

dict_tablas = {}
for letra, i in zip(alfabeto, range(6,28,7)):
    df = df1[i]
    df.pop("Dif.")
    dict_tablas[f'Grupo {letra}'] = df 

dict_tablas["Grupo A"][3:4]= ([['Canada', 0, 0, 0, 0, 0, 0, 0]])
dict_tablas["Grupo D"][3:4]= ([['Costa Rica', 0, 0, 0, 0, 0, 0, 0]])

with open("dict_table","wb") as output:
    pickle.dump(dict_tablas,output)
