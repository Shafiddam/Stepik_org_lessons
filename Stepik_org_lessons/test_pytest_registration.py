# 3.2 Тестирование web-приложений и тестовые фреймворкиЗадание: оформляем тесты в стиле unittest
# https://stepik.org/lesson/36285/step/13?unit=162401

# Попробуйте оформить тесты из первого модуля в стиле unittest.
# Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
# Создайте новый файл
# Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
# Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
# Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
# Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
# Запустите получившиеся тесты из файла
# Просмотрите отчёт о запуске и найдите последнюю строчку
# Отправьте эту строчку в качестве ответа на это задание
# Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте.
# Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае, здесь)!

from selenium import webdriver
from time import sleep
import unittest

class Test_registration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath("//input[@placeholder = 'Input your first name']")  # First name*
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[@placeholder = 'Input your last name']")  # Last name*
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//input[@placeholder = 'Input your email']")  # Email*
        input3.send_keys("1@ya.ru")
        #sleep(3)

        button = browser.find_element_by_css_selector("button.btn").click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        #assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Тест1 пройден")

        #sleep(3)
        #browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath("//input[@placeholder = 'Input your first name']")  # First name*
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[@placeholder = 'Input your last name']")  # Last name*
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//input[@placeholder = 'Input your email']")  # Email*
        input3.send_keys("1@ya.ru")
        #sleep(3)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn").click()
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        #assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(welcome_text, "NoSuchElementException", "Тест2 пройден")

        #sleep(3)
        #browser.quit()

if __name__ == "__main__":
    unittest.main()