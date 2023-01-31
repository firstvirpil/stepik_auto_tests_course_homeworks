import time
from math import sin, log

from selenium import webdriver
from selenium.webdriver.common.by import By


"""
    Открыть страницу http://suninjuly.github.io/redirect_accept.html
    Нажать на кнопку
    Переключиться на новую вкладку
    Пройти капчу для робота и получить число-ответ
"""

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Нажать на кнопку Submit.
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # Пройти капчу для робота и получить число-ответ
    x = int(browser.find_element(By.ID, 'input_value').text)
    print(x, type(x))
    y = log(abs(12*sin(x)))
    browser.find_element(By.XPATH, "//input[@type='text']").send_keys(y)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
#    browser.find_element(By.XPATH, "//span[@id='input_value']")

finally:
    time.sleep(6)
    browser.quit()
