from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math


'''Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент - картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x(сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".
'''

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    value_x = int(browser.find_element(By.XPATH, "//img").get_attribute('valuex'))
    # Посчитать математическую функцию от x (код для этого приведён ниже).
    value = calc(value_x)
    # print(value_x, value)

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
    sub = browser.find_element(By.XPATH, "//button[@type='submit']")
    sub.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
