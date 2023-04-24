
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# #Lee usuario un contraseña:
# credenciales_excel = r"./credenciales.xlsx"
# df = pd.read_excel(credenciales_excel)
# user = df["username"][0]
# psw = df["password"][0]

# instancias = r"./instancias.xlsx"
# df_instancias = pd.read_excel(instancias)

# print(df_instancias["Url"][0])


# inicializar driver:

def rpa_msc(user, psw, url):

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)


    #url = "https://app.myskillcamp.com/organize/WFlwQjJ1cEQ1a1dQN3JCQjllRUJHUT09/camp" #INCURSO
    #url = "https://app.myskillcamp.com/organize/d3lTcTMzMUVzY1Y4ZDNLd3pyOC80QT09/camp"
    #url= "https://app.myskillcamp.com/organize/WHlSTWd3K0YvS0ltWXBOcTJUd2x1dz09/camp" #UMB

    driver.get(url)
    driver.maximize_window()


    # Wait until page loads:
    wait_page = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/div/input')))

    # Ejecutar la acción después de que la página se haya cargado completamente
    if wait_page.is_displayed():
        # Input email:
        driver.find_element(By.XPATH, '//*[@id="login"]/div/input').send_keys(user)
        # Next buttom:
        driver.find_element(By.XPATH, '//*[@id="main"]/msc-login/div/div[2]/div/form/div/div[2]/msc-button/button').click()
    else:
        print("La página no se ha cargado completamente.")


    # Wait input password:
    imput_password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div/input')))

    # Ejecutar la acción después de que la página se haya cargado completamente
    if imput_password.is_displayed():
        # Input password:
        driver.find_element(By.XPATH, '//*[@id="password"]/div/input').send_keys(psw)
        driver.find_element(By.XPATH, '//*[@id="main"]/msc-login/div/div[2]/div/form/div/div[3]/msc-button/button').click()
    else:
        print("La página no se ha cargado completamente.")


    # Wait Statistics:
    wait_statisctics = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/msc-organize/msc-sidebar/ul/li[6]/i')))
    if wait_statisctics.is_displayed():
        # Input password:
        driver.find_element(By.XPATH, '//*[@id="main"]/msc-organize/msc-sidebar/ul/li[6]/i').click()
    else:
        print("La página no se ha cargado completamente.")


    # Wait Data Exports:
    wait_data_exports = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/msc-organize/section/msc-organize-statistic/div/msc-common-nav/nav/msc-common-tree/dl/dd[2]/div/div[1]/a')))
    if wait_data_exports.is_displayed():
        # Input password:
        driver.find_element(By.XPATH, '//*[@id="main"]/msc-organize/section/msc-organize-statistic/div/msc-common-nav/nav/msc-common-tree/dl/dd[2]/div/div[1]/a').click()
    else:
        print("La página no se ha cargado completamente.")


    # Download Learner overview report 

    driver.find_element(By.XPATH, '//*[@id="main"]/msc-organize/section/msc-organize-statistic/div/section/msc-exports/div/div[2]/div/msc-button[1]/button').click()

    # Wait Send Buttom:
    wait_send_buttom = wait.until(EC.presence_of_element_located((By.ID, 'cdk-overlay-26')))
    if wait_send_buttom.is_displayed():
        # Input password:
        driver.find_element(By.XPATH, '//*[@id="cdk-dialog-0"]/div/div[2]/div[3]/div/msc-button').click()
    else:
        print("La página no se ha cargado completamente.")

    # Wait ok Buttom:
    wait_ok_buttom = wait.until(EC.presence_of_element_located((By.ID, 'cdk-overlay-27')))
    if wait_ok_buttom.is_displayed():
        # Input password:
        driver.find_element(By.XPATH, '//*[@id="cdk-dialog-1"]/div/div[2]/div/msc-button/button').click()
    else:
        print("La página no se ha cargado completamente.")



    # Download Learner engagement report 

    driver.find_element(By.XPATH, '//*[@id="main"]/msc-organize/section/msc-organize-statistic/div/section/msc-exports/div/div[3]/div/msc-button[1]/button').click()

    # Wait Send Buttom:
    wait_send_buttom = wait.until(EC.presence_of_element_located((By.ID, 'cdk-overlay-28')))
    if wait_send_buttom.is_displayed():
        # Input password:
        driver.find_element(By.XPATH, '//*[@id="cdk-dialog-2"]/div/div[2]/div[3]/div/msc-button/button').click()
    else:
        print("La página no se ha cargado completamente.")

    # Wait ok Buttom:
    wait_ok_buttom = wait.until(EC.presence_of_element_located((By.ID, 'cdk-overlay-30')))
    if wait_ok_buttom.is_displayed():
        # Input password:
        driver.find_element(By.XPATH, '//*[@id="cdk-dialog-3"]/div/div[2]/div/msc-button/button').click()
    else:
        print("La página no se ha cargado completamente.")



    time.sleep(10)
    # Cerrar el driver de Selenium
    driver.quit()
