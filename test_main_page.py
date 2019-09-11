from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_new_guest_basket_page()


#     В файл test_main_page.py добавьте тест с названием
#  test_guest_cant_see_product_in_basket_opened_from_main_page:
#
#     Гость открывает главную страницу
#     Переходит в корзину по кнопке в шапке сайта
#     Ожидаем, что в корзине нет товаров
#     Ожидаем, что есть текст о том что корзина пуста
#
# В файле test_product_page.py добавьте тест с названием
# test_guest_cant_see_product_in_basket_opened_from_product_page:
#
#     Гость открывает страницу товара
#     Переходит в корзину по кнопке в шапке
#     Ожидаем, что в корзине нет товаров
#     Ожидаем, что есть текст о том что корзина пуста
#
# В классе BasePage реализуйте соответствующий метод для перехода в корзину. Создайте файл basket_page.py и в нем класс
# BasketPage. Реализуйте там необходимые проверки, в том числе отрицательную, которую мы обсуждали в предыдущих шагах.
# Убедитесь, что тесты проходят и зафиксируйте изменения в коммите.
