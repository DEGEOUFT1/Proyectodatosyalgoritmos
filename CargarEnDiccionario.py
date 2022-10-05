import pandas as pd
import numpy as np

callesmedellinacoso = pd.read_csv('https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/calles_de_medellin_con_acoso.csv', sep=';')
print(callesmedellinacoso)
ame  ...                                           geometry
0                                               Calle 10  ...  LINESTRING (-75.5728593 6.2115169, -75.5724984...
1                                               Calle 10  ...  LINESTRING (-75.5705202 6.2106275, -75.570427 ...
2                                            Carrera 43A  ...  LINESTRING (-75.5705202 6.2106275, -75.5705604...
3                                             Carrera 41  ...  LINESTRING (-75.5687719 6.2099661, -75.5688021...
4                                               Calle 10  ...  LINESTRING (-75.5687719 6.2099661, -75.568715 ...
...                                                  ...  ...                                                ...
68744                            Medellín - San Jerónimo  ...  LINESTRING (-75.7086893 6.3627057, -75.7087245...
68745                                                NaN  ...  LINESTRING (-75.7086893 6.3627057, -75.7087739...
68746                              San Jerónimo-Medellín  ...  LINESTRING (-75.6909483 6.338773, -75.6902973 ...
68747  ['Medellín - San Jerónimo', 'San Jerónimo-Mede...  ...  LINESTRING (-75.6909483 6.338773, -75.6918575 ...
68748                            Medellín - San Jerónimo  ...  LINESTRING (-75.6909483 6.338773, -75.69181519...

[68749 rows x 7 columns]



poligono = pd.read_csv('https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/poligono_de_medellin.csv', sep=';')
print(poligono)

geometry  ...  importance
0  POLYGON ((-75.7193741 6.34168, -75.7193637 6.3...  ...    0.923478

[1 rows x 14 columns]
