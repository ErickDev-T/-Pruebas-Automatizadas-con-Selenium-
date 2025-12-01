from utilities.driver_setup import get_driver
from utilities.helpers import take_screenshot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def test_vacaciones_create():
    driver = get_driver()
    driver.get("http://localhost:3000")  # tu URL

    driver.find_element(By.XPATH, "//input[@placeholder='Código del empleado']").send_keys("48454")

    driver.find_element(By.XPATH, "//button[text()='Buscar']").click()

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Nombre:')]")
        )
    )

    driver.find_element(By.XPATH, "//input[@wfd-id='id1']").send_keys("12-2-2025")

    driver.find_element(By.XPATH, "//input[@wfd-id='id2']").send_keys("5")


    driver.find_element(By.XPATH, "//button[text()='Calcular']").click()

    driver.find_element(By.XPATH, "//button[normalize-space()='Guardar']").click()

    wait = WebDriverWait(driver, 10)  # espera máx 10 segundos
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Vacaciones guardadas exitosamente')]")
        )
    )

    take_screenshot(driver, "vacaciones_save_ok")

    driver.quit()
