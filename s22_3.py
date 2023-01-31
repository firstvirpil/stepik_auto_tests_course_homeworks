from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select




'''
    Открыть страницу https://suninjuly.github.io/selects1.html
    Посчитать сумму заданных чисел
    Выбрать в выпадающем списке значение равное расчитанной сумме
    Нажать кнопку "Submit"

'''

try:
    def calc(x,y):
        return x + y


    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    value_x = int(browser.find_element(By.XPATH, "//span[@id='num1']").text)
    value_y = int(browser.find_element(By.XPATH, "//span[@id='num2']").text)
    # Посчитать математическую функцию от x (код для этого приведён ниже).
    value = str(calc(value_x, value_y))
    print(value)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value)  # ищем элемент с текстом

    # Нажать на кнопку Submit.
    sub = browser.find_element(By.XPATH, "//button[@type='submit']")
    sub.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
