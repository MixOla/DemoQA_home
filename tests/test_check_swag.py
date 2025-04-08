from conftest import browser
from pages.swag_labs import SwagLabs
from pages.swag_labs import BasePage


def test_icon_exist(browser):
    suacedomo_page = SwagLabs(browser)
    suacedomo_page.visit()
    assert suacedomo_page.exist_icon() is True, "Иконка не найдена"


def test_icon_exist(browser):
    "Проверяет наличие иконки"
    suacedomo_page = SwagLabs(browser)
    suacedomo_page.visit()
    assert suacedomo_page.exist_icon() is True, "Иконка не найдена"

def test_icon_username_exist(browser):
    "Проверяет наличие поля имени"
    suacedomo_page = SwagLabs(browser)
    suacedomo_page.visit()
    assert suacedomo_page.exist_username() is True, "Поле имени не найдено"

def test_icon_password_exist(browser):
    "Проверяет наличие поля пароля"
    suacedomo_page = SwagLabs(browser)
    suacedomo_page.visit()
    assert suacedomo_page.exist_password() is True, "Поле пароля не найдено"