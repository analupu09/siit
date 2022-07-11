import json

import wait as wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def kayak_website():
    data = []
    url = f'https://www.kayak.ie/flights/BUH-TYO/2022-08-12/2022-08-26'
    driver = webdriver.Chrome()
    driver.set_window_size(960, 900)
    driver.set_window_position(0, 0)
    driver.get(url)
    wait = WebDriverWait(driver, 30)
    original_window = driver.current_window_handle

    accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="apCq"]/div[13]/div/div[3]/div/div/div[1]')))
    accept_button.click()


    tickets_kayak = driver.find_elements(By.XPATH, '//div[@class="resultWrapper"]')
    for index, ticket_kayak in enumerate(tickets_kayak):
        departure_kayak = ticket_kayak.find_element(By.XPATH, '//li[@class="flight with-gutter"]//div[@class="section times"]//div[@class="top"]//span[@class="depart-time base-time"]').text
        return_kayak = ticket_kayak.find_element(By.XPATH, '//li[@class="flight "]//div[@class="section times"]//div[@class="top"]//span[@class="depart-time base-time"]').text
        price_kayak = ticket_kayak.find_element(By.XPATH, '//span[@class="price option-text"]').text

        time.sleep(10)
        data.append({
            'kayak_departure_time': departure_kayak,
            'kayak_return_time': return_kayak,
            'kayak_prices': price_kayak
        })
    time.sleep(10)
    driver.quit()

    with open('kayak_results.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

kayak_website()

