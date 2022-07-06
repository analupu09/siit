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
            driver.execute_script('window.scrollTo(0,50)')
            time.sleep(10)
            for opodo_prices in flight_details1:
                data.append({
                    'flight_price_opodo': opodo_prices.text
                })

        else:
            driver.set_window_size(940, 900)
            driver.set_window_position(970, 0)
            driver.get(url)
            accept_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')))
            accept_button.click()
            flight_details2 = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="mainView"]/div/div/div[2]/ith-flight-offers/div/div[1]/div/div/ith-flight-offer/div/div/div[2]/ith-flight-offer-actions/div/div/strong')))
            for vola_prices in flight_details2:
                data.append({
                    'flight_prices_vola': vola_prices.text
                })

    driver.quit()

    with open('output.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)
