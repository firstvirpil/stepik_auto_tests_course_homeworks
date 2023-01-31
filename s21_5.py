from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math





""" Открыть страницу https://suninjuly.github.io/math.html.
    Считать значение для переменной x.
    Посчитать математическую функцию от x (код для этого приведён ниже).
    Ввести ответ в текстовое поле.
    Отметить checkbox "I'm the robot".
    Выбрать radiobutton "Robots rule!".
    Нажать на кнопку Submit.
"""
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    value_x = browser.find_element(By.XPATH, "//span[@id='input_value']").text
    # Посчитать математическую функцию от x (код для этого приведён ниже).
    value_x = int(value_x)
    value = calc(value_x)
    value = str(value)
    print(type(value), value)

    # Ввести ответ в текстовое поле.
    tex = browser.find_element(By.XPATH, "//input[@id='answer']")
    tex.send_keys(value)
    # Отметить checkbox "I'm the robot".
    checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']")
    checkbox.click()
    # Выбрать radiobutton "Robots rule!".
    checkbox = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    checkbox.click()
    # Нажать на кнопку Submit.
    submi = browser.find_element(By.XPATH, "//button[@type='submit']")
    submi.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
