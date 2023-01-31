import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
    Открыть страницу http://suninjuly.github.io/file_input.html
    Заполнить текстовые поля: имя, фамилия, email
    Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    Нажать кнопку "Submit"
"""


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    first_name = browser.find_element(By.XPATH, '//input[@name="firstname"]')
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.XPATH, '//input[@name="lastname"]')
    last_name.send_keys("Petrov")
    email = browser.find_element(By.XPATH, '//input[@name="email"]')
    email.send_keys("Smolensk@mai.mm")
    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    with open("file.txt", 'w') as file:
        file.write("empty11")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.XPATH, '//input[@name="file"]').send_keys(file_path)
    # Нажать на кнопку Submit.
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
