import pandas as pd
import time
from rpa import rpa_msc


#Lee usuario y contraseña:
credenciales_excel = r"./credenciales.xlsx"
df = pd.read_excel(credenciales_excel)
user = df["username"][0]
psw = df["password"][0]

#Lee instancias.xlsx
instancias = r"./instancias.xlsx"
df_instancias = pd.read_excel(instancias)


#Ciclo para descarga de información:

# for url_instancia in df_instancias["Url"]:
#     rpa_msc(user, psw, url_instancia)
#     time.sleep(5)
    

for index, row in df_instancias.iterrows():
    nombre = row["Nombre"]
    url = row["Url"]
    rpa_msc(user, psw, url, nombre)
    time.sleep(5)
