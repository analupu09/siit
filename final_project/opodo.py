import json
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


if __name__ == '__main__':
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 30)
    driver.get('https://www.opodo.com/travel/#results/type=R;from=BUH;to=TYO;dep=2022-08-12;ret=2022-08-26;buyPath=FLIGHTS_HOME_SEARCH_FORM;internalSearch=true')
    driver.set_window_size(960, 900)
    driver.set_window_position(0, 0)
    agree_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="didomi-notice-agree-button"]')))
    agree_button.click()
    data = []
    tickets = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div')))
    print("tickets", tickets)
    for index, ticket in enumerate(tickets):
        try:
            opodo_hours = driver.find_elements(By.XPATH, '//div[@class="css-v0s8x5-BaseText-Body e8tl7c60"]').text
        except NoSuchElementException:
            opodo_hours = None
        try:
            opodo_prices = wait.until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                                '//*[contains(@class, "money-integer css-1umyyay-BaseText-MoneyPart-DefaultPart e16uabde1")]'))).text
        except NoSuchElementException:
            opodo_prices = None
        flight_data = {
            "website": "Opodo",
            "info": {
                "flight_hours": opodo_hours,
                "flight_prices": opodo_prices
            }
        }
        time.sleep(15)
        data.append(flight_data)
        print(index)

    driver.close()

    with open('output.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)


