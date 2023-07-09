
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def rpa_msc(user, psw, url, name):

    #Initial result list:
    results = []
    results.append(("Name","Step", "Status", "Detail"))

    ###-------------------------------------------------------------###
    ###-------------------------------------------------------------###
    ###-------------------------------------------------------------###
    
    # 1-Initialize driver:

    try:
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 50)
        results.append((str(name),"1-Initialize Driver", "Successful"))
    except Exception as error:
        error = str(error).replace("\n", "")
        results.append((str(name),"1-Initialize Driver", "Unsuccessful:", str(error)))

    ###-------------------------------------------------------------###
    ###-------------------------------------------------------------###
    ###-------------------------------------------------------------###

    # 2-Get Url
    try:
        driver.get(url)
        driver.maximize_window()
        results.append((str(name),"2-Get Url", "Successful"))
    except Exception as error:
        error = str(error).replace("\n", "")
        results.append((str(name),"2-Get Url", "Unsuccessful", str(error)))

    ###-------------------------------------------------------------###
    ###-------------------------------------------------------------###
    ###-------------------------------------------------------------###

    # 3-Login

    try:
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

        results.append((str(name),"3-Login", "Successful"))

    except Exception as error:
        error = str(error).replace("\n", "")
        results.append((str(name),"3-Login", "Unsuccessful", str(error)))


    ###-------------------------------------------------------------###
    ###-------------------------------------------------------------###
    ###-------------------------------------------------------------###

    #4-Load Statistics section

    try:
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

        results.append((str(name),"4-Load Statistics section", "Successful"))

    except Exception as error:
        error = str(error).replace("\n", "")
        results.append((str(name),"4-Load Statistics section", "Successful", str(error)))


    ###-------------------------------------------------------------###
    ###-------------------------------------------------------------###
    ###-------------------------------------------------------------###



    #5-Download Learner overview report 

    try:
        driver.find_element(By.XPATH, '//*[@id="main"]/msc-organize/section/msc-organize-statistic/div/section/msc-exports/div/div[2]/div/msc-button[1]/button').click()

        # Wait Send Buttom:
        wait_send_buttom = wait.until(EC.presence_of_element_located((By.ID, 'cdk-overlay-26')))
        if wait_send_buttom.is_displayed():
            # Input password:
            try:
                driver.find_element(By.XPATH, '//*[@id="cdk-dialog-0"]/div/div[2]/div[3]/div/msc-button').click()
            except:
                driver.find_element(By.XPATH, '//*[@id="cdk-dialog-0"]/div/div[2]/div[3]/div/msc-button/button').click()
        else:
            print("La página no se ha cargado completamente.")

        # Wait ok Buttom:
        wait_ok_buttom = wait.until(EC.presence_of_element_located((By.ID, 'cdk-overlay-27')))
        if wait_ok_buttom.is_displayed():
            # Input password:
            driver.find_element(By.XPATH, '//*[@id="cdk-dialog-1"]/div/div[2]/div/msc-button/button').click()
        else:
            print("La página no se ha cargado completamente.")

        results.append((str(name),"5-Download Learner overview report", "Successful"))

    except Exception as error:
        error = str(error).replace("\n", "")
        results.append((str(name),"5-Download Learner overview report", "Successful", str(error)))


    ###-------------------------------------------------------------###
    ###-------------------------------------------------------------###
    ###-------------------------------------------------------------###

    time.sleep(5)


    #6-Download Learner engagement report 

    try:
        
        try:
            driver.find_element(By.XPATH, '//*[@id="main"]/msc-organize/section/msc-organize-statistic/div/section/msc-exports/div/div[3]/div/msc-button[1]/button').click()
        except:
            driver.find_element(By.XPATH, '//*[@id="cdk-dialog-0"]/div/div[2]/div[3]/div/msc-button/button').click()


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

        results.append((str(name),"6-Download Learner engagement report", "Successful"))

    except Exception as error:
        error = str(error).replace("\n", "")
        results.append((str(name),"6-Download Learner engagement report", "Successful", str(error)))


    ###-------------------------------------------------------------###
    ###-------------------------------------------------------------###
    ###-------------------------------------------------------------###

    # Añadir una pausa y Cerrar el driver de Selenium
    time.sleep(2)

    # Make results file:
    for i in results:
        print(i)

    with open("results.csv", "w") as archivo:
       
        for row in results:
            # Comprobar la longitud de la fila
            if len(row) == 4:
                name, step, status, detail = row
                archivo.write(name + "," + step + "," + status + "," + detail + "\n")
            elif len(row) == 3:
                name, step, status = row
                archivo.write(name + "," + step + "," + status + "\n")


    driver.quit()


###-------------------------------------------------------------###
###-------------------------------------------------------------###
###-------------------------------------------------------------###


# import pandas as pd
# import time
# from rpa import rpa_msc


# #Lee usuario y contraseña:
# credenciales_excel = r"./credenciales.xlsx"
# df = pd.read_excel(credenciales_excel)
# user = df["username"][0]
# psw = df["password"][0]

# #Lee instancias.xlsx
# instancias = r"./instancias.xlsx"
# df_instancias = pd.read_excel(instancias)


# #Ciclo para descarga de información:

# for index, row in df_instancias.iterrows():
#     nombre = row["Nombre"]
#     url = row["Url"]
#     rpa_msc(user, psw, url, nombre)
#     time.sleep(5)

    