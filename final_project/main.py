from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


if __name__ == '__main__':
    data = []

    URLS = ('https://www.opodo.com/travel/#results/type=R;from=BUH;to=TYO;dep=2022-08-12;ret=2022-08-26;buyPath=FLIGHTS_HOME_SEARCH_FORM;internalSearch=true',
            'https://www.cheapflights.co.uk/flight-search/BUH-TYO/2022-07-28/2022-08-10')
    first = True
    for url in URLS:
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 20)
        original_window = driver.current_window_handle
        if first:
            driver.set_window_size(960, 900)
            driver.set_window_position(0, 0)
            driver.get(url)
            agree_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="didomi-notice-agree-button"]')))
            agree_button.click()
            time.sleep(4)
            first = False
        else:
            driver.set_window_size(940, 900)
            driver.set_window_position(970, 0)
            driver.get(url)
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="PtXs"]/div[12]/div/div[3]/div/div/div[2]/div/div/div[1]/button/div[1]/div'))).click()
            time.sleep(5)


