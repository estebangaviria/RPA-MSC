import selenium
import pandas as pd
from selenium import webdriver



#Lee usuario un contraseña:
credenciales_excel = r"D:\PROYECTOS\ROBOT GRIKY\credenciales.xlsx"
df = pd.read_excel(credenciales_excel)
user = df["username"][0]
psw = df["password"][0]


# inicializar driver:

driver = webdriver.Chrome()


url = "https://app.myskillcamp.com/organize/WFlwQjJ1cEQ1a1dQN3JCQjllRUJHUT09/camp"

driver.get(url)
driver.maximize_window()