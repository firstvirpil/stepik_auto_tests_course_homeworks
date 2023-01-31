
from selenium import webdriver

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

# browser.switch_to.window(window_name)

new_window = browser.window_handles[1]
first_window = browser.window_handles[0]

current_window = browser.current_window_handle
