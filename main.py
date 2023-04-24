
import pandas as pd
import time
from rpa import rpa_msc


#Lee usuario un contraseña:
credenciales_excel = r"./credenciales.xlsx"
df = pd.read_excel(credenciales_excel)
user = df["username"][0]
psw = df["password"][0]

#Lee instancias.xlsx

instancias = r"./instancias.xlsx"
df_instancias = pd.read_excel(instancias)


for url_instancia in df_instancias["Url"]:
    rpa_msc(user, psw, url_instancia)
    

