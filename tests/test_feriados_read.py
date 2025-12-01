from utilities.driver_setup import get_driver
from utilities.helpers import take_screenshot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def test_vacaciones_create():
    driver = get_driver()
    driver.get("http://localhost:3000")

    no_feriados = (By.XPATH, "//*[contains(text(), 'No hay feriados registrados')]")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.invisibility_of_element_located(no_feriados))

    take_screenshot(driver, "feriado_read_ok")

