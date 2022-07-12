import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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

    time.sleep(10)
    driver.find_element(By.XPATH, '//button/div[1]/div[text()="Accept"]').find_element(By.XPATH, '../..').click()
    time.sleep(10)

    tickets_kayak = driver.find_elements(By.XPATH, '//div[@class="resultWrapper"]')
    for index, ticket_kayak in enumerate(tickets_kayak):
        departure_time = ticket_kayak.find_element(By.XPATH, './/div[contains(@class, "Flights-Results-ResultInfo multiple-legs")]/ol/li[1]/div/div/div[contains(@class, "times")]/div/span[contains(@class, "time-pair")]/span[contains(@class, "depart-time")]').text
        departure_arrival_time = ticket_kayak.find_element(By.XPATH, './/div[contains(@class, "Flights-Results-ResultInfo multiple-legs")]/ol/li[1]/div/div/div[contains(@class, "times")]/div/span[contains(@class, "time-pair")]/span[contains(@class, "arrival-time")]').text
        return_time = ticket_kayak.find_element(By.XPATH, './/div[contains(@class, "Flights-Results-ResultInfo multiple-legs")]/ol/li[2]/div/div/div[contains(@class, "times")]/div/span[contains(@class, "time-pair")]/span[contains(@class, "depart-time")]').text
        return_arrival_time = ticket_kayak.find_element(By.XPATH, './/div[contains(@class, "Flights-Results-ResultInfo multiple-legs")]/ol/li[2]/div/div/div[contains(@class, "times")]/div/span[contains(@class, "time-pair")]/span[contains(@class, "arrival-time")]').text
        flight_price = ticket_kayak.find_element(By.XPATH, './/span[@class="price-text"]').text

        data.append({
            'kayak_departure_time': departure_time,
            'kayak_departure_arrival_time': departure_arrival_time,
            'kayak_return_time': return_time,
            'kayak_return_arrival_time': return_arrival_time,
            'kayak_prices': flight_price
        })

    driver.quit()

    with open('kayak_results.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

kayak_website()