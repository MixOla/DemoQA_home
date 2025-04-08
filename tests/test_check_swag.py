from conftest import browser
from pages.swag_labs import SwagLabs
from pages.swag_labs import BasePage


def test_icon_exist(browser):
    suacedomo_page = BasePage(browser)
    suacedomo_page.visit()
    assert suacedomo_page.find_element(locator='#login-button')
