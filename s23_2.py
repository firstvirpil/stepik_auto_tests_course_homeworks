"""
только принять
переход на модальное окно и принятие
alert = browser.switch_to.alert
alert.accept()

получение
alert = browser.switch_to.alert
alert_text = alert.text

confirm да или нет
согласие
confirm = browser.switch_to.alert
confirm.accept()

или отказ - Отмена
confirm.dismiss()

prompt да.нет.ввод текста
ввод текста
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
"""