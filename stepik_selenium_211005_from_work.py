''' 1 задание
import math
fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
print(fun(5))
'''




'''import time
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://kzn.rpa-mu.ru/")
time.sleep(1)

textarea = driver.find_element_by_css_selector("/Users/Account/LogOn?ReturnUrl=%2F")
#textarea = driver.find_element_by_css_selector(".textbox")
submit_button.click()
'''





'''
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
# закрываем браузер после всех манипуляций
    browser.quit()
'''




'''
#https://stepik.org/lesson/138920/step/4?unit=196194
from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")

    button = browser.find_element_by_id("submit_button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла (для линукса)
'''







'''
#https://stepik.org/lesson/138920/step/5?unit=196194
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"

browser = webdriver.Chrome()
browser.get(link)

#str(math.ceil(math.pow(math.pi, math.e)*10000))

link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
link.click()

input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name("city")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")

button = browser.find_element_by_tag_name("button")
button.click()
time.sleep(30)
'''








'''
#https://stepik.org/lesson/138920/step/7?unit=196194
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys("_")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
'''







'''
# https://stepik.org/lesson/138920/step/8?unit=196194
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")

    element = browser.find_element_by_xpath("//button[@type = 'submit']").click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
'''







'''
# Уникальность селекторов: часть 2
# https://stepik.org/lesson/138920/step/10?unit=196194

from selenium import webdriver
from time import sleep

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("//input[@placeholder = 'Input your first name']") # First name*
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@placeholder = 'Input your last name']") # Last name*
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//input[@placeholder = 'Input your email']") # Email*
    input3.send_keys("1@ya.ru")
    sleep(3)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
'''





# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
# https://stepik.org/lesson/165493/step/5

from selenium import webdriver
from time import sleep
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_xpath("//div/label/span[@id = 'input_value']").text
    y = calc(x)
    browser.find_element_by_xpath("//[@id = answer']").send_keys(y)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()


