from selenium import webdriver
#Sirve para usar localizadores
from selenium.webdriver.common.by import By
#Sirve para usar sleep
import time

#Función
def test_login_exitoso():

    #Abré navegador
    driver = webdriver.Chrome()

    #Ingresá a url
    driver.get("https://www.saucedemo.com/")

    #Localizar elementos de la primera pantalla
    usuario = driver.find_element(By.ID,"user-name")
    password = driver.find_element(By.ID,"password")
    boton_login = driver.find_element(By.ID,"login-button")

    #Completar el formulario
    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")

    time.sleep(2)

    boton_login.click()

    time.sleep(1)
    #Locanliza el elemente de la 2da pantalla(Inventory)
        #titulo = driver.find_element(By.CLASS_NAME,"app_logo")
        #titulo = driver.find_element(By.CSS_SELECTOR,".header_label > .app_logo")
    titulo = driver.find_element(By.CSS_SELECTOR,"[data-test='title']")

    #Validar el URL despues de login
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    #assert titulo.text == "Swag Labs" 
    assert titulo.text == "Products" 

    #Cierro navegador
    driver.quit()


    #Simulamos una espera por consola
    #input("Presiona ENTER para cerrar...")