"""
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене.
Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

    Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    Нажать на кнопку "Book"
    Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
"""
import time
from math import sin, log


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
# говорим Selenium проверять в течение 15 секунд, пока
WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
button_book = browser.find_element(By.ID, "book")
button_book.click()
x = int(browser.find_element(By.ID, 'input_value').text)
y = log(abs(12*sin(x)))
browser.find_element(By.ID, "answer").send_keys(y)
browser.find_element(By.ID, "solve").click()

time.sleep(5)
browser.quit()
