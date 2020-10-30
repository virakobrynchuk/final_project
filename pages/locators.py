from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")


class LoginPageLocators():
    LOGIN_USERNAME_FORM = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS_FORM = (By.CSS_SELECTOR, "#id_login-password")
    REG_EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS1_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS2_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form .btn")


class BasketPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
