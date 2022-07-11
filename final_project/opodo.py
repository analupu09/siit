import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def opodo_website():
    data = []
    url = f'https://www.opodo.com/travel/#results/type=R;from=BUH;to=TYO;dep=2022-08-12;ret=2022-08-26;buyPath=FLIGHTS_HOME_SEARCH_FORM;internalSearch=true'
    driver = webdriver.Chrome()
    driver.set_window_size(960, 900)
    driver.set_window_position(0, 0)
    driver.get(url)
    wait = WebDriverWait(driver, 30)
    original_window = driver.current_window_handle

    agree_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="didomi-notice-agree-button"]')))
    agree_button.click()

    flight_price_opodo = wait.until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                                '//*[contains(@class, "money-integer css-1umyyay-BaseText-MoneyPart-DefaultPart e16uabde1")]')))
    for prices_opodo in flight_price_opodo:
        data.append({
            'flight_price_opodo': prices_opodo.text
        })

    driver.quit()

    with open('opodo_results.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

opodo_website()