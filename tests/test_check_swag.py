from pages.swag_labs import SwagLabs


def test_icon_exist(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_icon()


def test_username_exist(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_username()


def test_password_exist(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_password()
