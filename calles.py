import pandas as pd
import numpy as np

callesmedellinacoso = pd.read_csv('https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/calles_de_medellin_con_acoso.csv', sep=';')
print(callesmedellinacoso)

poligono = pd.read_csv('https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/poligono_de_medellin.csv', sep=';')
print(poligono)