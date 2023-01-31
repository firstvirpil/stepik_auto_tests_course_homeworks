import time
from math import sin, log

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
    Открыть страницу http://SunInJuly.github.io/execute_script.html.
    Считать значение для переменной x.
    Посчитать математическую функцию от x.
    Проскролить страницу вниз.
    Ввести ответ в текстовое поле.
    Выбрать checkbox "I'm the robot".
    Переключить radiobutton "Robots rule!".
    Нажать на кнопку "Submit".
"""

#
# def ln(item):
#     return abs(12*sin(value_x))


try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)
    # Считать значение для переменной x.
    value_x = int(browser.find_element(By.XPATH, "//span[@id='input_value']").text)
    # Посчитать математическую функцию от x
    value = log(abs(12*sin(value_x)))
    # Проскролить страницу вниз. используем "return arguments[0].scrollIntoView(true);" пример ниже
    '''
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    '''
    # button_submit = browser.find_element(By.XPATH, "//button[@type='submit']")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
    # Ввести ответ в текстовое поле
    browser.find_element(By.XPATH, "//input[@type='text']").send_keys(value)
    # Выбрать checkbox "I'm the robot"
    browser.find_element(By.XPATH, "//input[@id='robotCheckbox']").click()
    # Переключить radiobutton "Robots rule!" пришлось проскролить и потом нажать
    # browser.find_element(By.XPATH, "//input[@id='robotsRule']").click()
    robot = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot)
    robot.click()
    # Нажать на кнопку "Submit".
    but = browser.find_element(By.XPATH, "//button[@type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", but)
    but.click()
    # не работает такая строка, нужно скролить browser.find_element(By.XPATH, "//button[@type='submit']").click()


finally:
    time.sleep(10)
    browser.quit()