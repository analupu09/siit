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
    time.sleep(20)

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # scrollWait = WebDriverWait(driver, 2)
    # showMoreElementsButton = scrollWait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Show 30 more results"]')))
    # if showMoreElementsButton:
    #     showMoreElementsButton.click()
    #     time.sleep(5)


    tickets = driver.find_elements(By.XPATH, '//div[@data-testid="itinerary"]')
    print(len(tickets))
    # for index, ticket in enumerate(tickets):
    #     departure_time = ticket.find_element(By.XPATH,
    #                                               './/div/ith-flight-offer/div/div/div[1]/ith-flight-stage[1]/div/div[2]/div/div[1]/div[1]/div[1]/span').text
    #     departure_arrival_time = ticket.find_element(By.XPATH,
    #                                               './/div/ith-flight-offer/div/div/div[1]/ith-flight-stage[1]/div/div[2]/div/div[3]/div[1]/div[1]/span').text
        # arrival_time = ticket.find_element(By.XPATH,
        #                                         './/div/ith-flight-offer/div/div/div[1]/ith-flight-stage[2]/div/div[2]/div/div[1]/div[1]/div[1]/span').text
        #
        # arrival_departure_time = ticket.find_element(By.XPATH,
        #                                                   './/div/ith-flight-offer/div/div/div[1]/ith-flight-stage[2]/div/div[2]/div/div[3]/div[1]/div[1]/span').text
        # flight_price = ticket.find_element(By.XPATH,
        #                                         './/div/ith-flight-offer/div/div/div[2]/ith-flight-offer-actions/div/div/strong/span').text

        # data.append({
        #     'vola_flight_departure_time': departure_time,
        #     'vola_arrival_time': departure_arrival_time,
        #     'vola_flight_arrival': arrival_time,
        #     'vola_arrival_departure_time': arrival_departure_time,
        #     'vola_flight_prices': flight_price
        # })

    driver.quit()

    with open('opodo_results.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

opodo_website()