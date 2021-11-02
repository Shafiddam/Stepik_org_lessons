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
textarea.send_keys("Эти слова я написал на Питоне в своей программе, запустил эту программу и она должна сама написать этот текст и нажать кнопку отправить ")
time.sleep(1)
# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector("._4sWnG")
# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(1)
# После выполнения всех действий мы должны не забыть закрыть окно браузера
#driver.quit()
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







#https://stepik.org/lesson/138920/step/8?unit=196194
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

    #element = browser.find_element_by_xpath("//div[@class = 'btn' and button[text() = 'Submit']]").click()
    element = browser.find_element_by_xpath('//button[text() = "Submit")]').click()
    #element = browser.find_element_by_xpath("//button[text() = 'Submit']").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

