from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def open(self):
        super().open(self.URL)

    def login(self, username, password):
        self.find(self.USERNAME).send_keys(username)
        self.find(self.PASSWORD).send_keys(password)
        self.find(self.LOGIN_BTN).click()

    def is_inventory_visible(self):
        return self.find(self.INVENTORY_CONTAINER).is_displayed()

    def get_error_text(self):
        return self.find(self.ERROR_MSG).text
