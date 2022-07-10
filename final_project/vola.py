import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def vola_website():
    data = []
    url = f'https://www.vola.ro/flight_search/from/Bucure%C5%9Fti/to/Tokyo/from_code/BUH/to_code/TYO/dd/2022-08-12/rd/2022-08-26/ad/1'
    driver = webdriver.Chrome()
    driver.get(url)
    wait = WebDriverWait(driver, 30)
    original_window = driver.current_window_handle

    driver.set_window_size(940, 900)
    driver.set_window_position(970, 0)
    driver.implicitly_wait(10)
    driver.get(url)
    accept_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')))
    accept_button.click()
    # wait for website to load completely
    time.sleep(10)
    tickets_vola = driver.find_elements(By.XPATH, '//*[contains(@class, "flight-fade")]')
    for index, ticket_vola in enumerate(tickets_vola):
        departure_vola = ticket_vola.find_element(By.XPATH,
                                                  '//div[@class="checkpoint__primary"]//div[@class="checkpoint__hour"]//span[@ng-bind="::$ctrl.stage.departureHour"]').text

        return_vola = ticket_vola.find_element(By.XPATH,
                                               '//div[@class="flight-fade"]//div[@class="checkpoint__primary"]/div[@class="checkpoint__hour"]/span[@ng-bind="::$ctrl.stage.arrivalHour"]').text

        flight_price_vola = ticket_vola.find_element(By.XPATH,
                                                     '//div[@class="flight-fade"]//div[@class="pricing"]/strong[@class="price"]/span').text

        data.append({
            'vola_flight_departure_time': departure_vola,
            'vola_flight_return_time': return_vola,
            'vola_flight_prices': flight_price_vola
        })

    driver.quit()

    with open('output_vola.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

vola_website()
