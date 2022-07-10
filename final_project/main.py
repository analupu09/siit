import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == '__main__':
    data = []

    URLS = (
        'https://www.opodo.com/travel/#results/type=R;from=BUH;to=TYO;dep=2022-08-12;ret=2022-08-26;buyPath=FLIGHTS_HOME_SEARCH_FORM;internalSearch=true',
        'https://www.vola.ro/flight_search/from/Bucure%C5%9Fti/to/Tokyo/from_code/BUH/to_code/TYO/dd/2022-08-12/rd/2022-08-26/ad/1')
    first = True
    for url in URLS:
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 30)
        original_window = driver.current_window_handle
        if first:
            driver.set_window_size(960, 900)
            driver.set_window_position(0, 0)
            driver.get(url)
            agree_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="didomi-notice-agree-button"]')))
            agree_button.click()
            first = False
            flight_details1 = wait.until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                                '//*[contains(@class, "money-integer css-1umyyay-BaseText-MoneyPart-DefaultPart e16uabde1")]')))
            for opodo_prices in flight_details1:
                data.append({
                    'flight_price_opodo': opodo_prices.text
                })

        else:
            driver.set_window_size(940, 900)
            driver.set_window_position(970, 0)
            driver.implicitly_wait(10)
            driver.get(url)
            accept_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')))
            accept_button.click()

            departure_vola = driver.find_elements(By.XPATH, '//div[@class="checkpoint__primary"]//div[@class="checkpoint__hour"]//span[@ng-bind="::$ctrl.stage.departureHour"]')
            for vola_departure in departure_vola:
                data.append({
                    'vola_flight_departure_time': vola_departure.text,
                })
            time.sleep(10)
            arrival_vola = driver.find_elements(By.XPATH, '//div[@class="flight-fade"]//div[@class="checkpoint__primary"]/div[@class="checkpoint__hour"]/span[@ng-bind="::$ctrl.stage.arrivalHour"]')
            for vola_return in arrival_vola:
                data.append({
                    'vola_flight_return_time': vola_return.text
                })
            time.sleep(10)
            flight_details_vola = driver.find_elements(By.XPATH, '//div[@class="flight-fade"]//div[@class="pricing"]/strong[@class="price"]/span')
            for vola_prices in flight_details_vola:
                data.append({
                    'vola_flight_prices': vola_prices.text
                })
            time.sleep(10)

            # tickets = driver.find_elements(By.XPATH, '//div[@class="ith-flight-offer__flight"]')
            # for index, ticket in enumerate(tickets):
            #     departure_vola = driver.find_element(By.XPATH,
            #                                           '//div[@class="checkpoint__primary"]//div[@class="checkpoint__hour"]//span[@ng-bind="::$ctrl.stage.departureHour"]').text
            #     time.sleep(10)
            #     arrival_vola = driver.find_element(By.XPATH,
            #                                         '//div[@class="flight-fade"]//div[@class="checkpoint__primary"]/div[@class="checkpoint__hour"]/span[@ng-bind="::$ctrl.stage.arrivalHour"]').text
            #     time.sleep(10)
            #     flight_details_vola = driver.find_element(By.XPATH,
            #                                                '//div[@class="flight-fade"]//div[@class="pricing"]/strong[@class="price"]/span').text
            #     time.sleep(10)
            #     data.append({
            #         'vola_flight_departure_time': departure_vola,
            #         'vola_flight_return_time': arrival_vola,
            #         'vola_flight_prices': flight_details_vola
            #     })

    driver.quit()

    with open('output.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)
