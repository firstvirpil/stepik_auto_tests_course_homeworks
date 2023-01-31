from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
#Внимание файл chromedriver.exe должен находится в том же каталоге, что и скрипт, в противном случае необходимпо прописать путь к нему.
link = "http://suninjuly.github.io/registration2.html"
#"http://suninjuly.github.io/registration2.html" Обновленная страница приводящая к ошибке NoSuchElementException

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.second_class input")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
    input3.send_keys("Smolensk@ttt.ru")

    button = browser.find_element(By.XPATH, '//div/form/button')
    button.click()

    time.sleep(1)
    
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
  #  / html / body / div / h1 Congratulations! You have successfully registered!
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидаем 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

