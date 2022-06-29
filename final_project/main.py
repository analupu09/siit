from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    # first website
    driver.get('https://www.opodo.com/')

    agree_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="didomi-notice-agree-button"]')))
    agree_button.click()

    departure = driver.find_element(By.XPATH,
                                    '//*[@id="react-app"]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div/input')
    departure.send_keys('Bucharest', Keys.ENTER)
    time.sleep(2)

    arrival = driver.find_element(By.XPATH,
                                  '//*[@id="react-app"]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div/input')
    arrival.send_keys('Tokyo', Keys.ENTER)
    time.sleep(2)

    # departure details
    driver.find_element(By.XPATH,
                        '//*[@id="react-app"]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div/div[3]/div/div[1]/input').click()
    driver.find_element(By.XPATH,
                        '//*[@id="react-app"]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div/div[3]/div/div[2]/div/div[1]/div/div[3]/div/div[2]/div[5]/div[3]').click()

    # return details
    driver.find_element(By.XPATH,
                        '//*[@id="react-app"]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div/div[4]/div/div[1]/input').click()
    driver.find_element(By.XPATH,
                        '//*[@id="react-app"]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div/div[4]/div/div[2]/div/div[1]/div/div[3]/div/div[2]/div[6]/div[2]').click()

    # search flights
    driver.find_element(By.XPATH,
                        '//*[@id="react-app"]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div/div[4]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="react-app"]/div/div/div[1]/div/div[2]/div[1]/div[3]/div[2]/button').click()

    # second website
    driver.get('https://www.cheapflights.co.uk/')

    accept_cookies = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[4]/div/div[3]/div/div/div[2]/div/div/div[1]/button/div[1]/div'))).click()
