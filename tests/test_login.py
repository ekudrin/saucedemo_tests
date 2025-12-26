import allure

@allure.feature("Login")
class TestLogin:

    @allure.title("Успешный логин standard_user")
    def test_success_login(self, login_page):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert "inventory" in login_page.current_url
        assert login_page.is_inventory_visible()

    @allure.title("Логин с неверным паролем")
    def test_invalid_password(self, login_page):
        login_page.open()
        login_page.login("standard_user", "wrong_password")

        assert "Epic sadface" in login_page.get_error_text()

    @allure.title("Логин заблокированного пользователя")
    def test_locked_user(self, login_page):
        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")

        assert "locked out" in login_page.get_error_text()

    @allure.title("Логин с пустыми полями")
    def test_empty_fields(self, login_page):
        login_page.open()
        login_page.login("", "")

        assert "Username is required" in login_page.get_error_text()

    @allure.title("Логин performance_glitch_user")
    def test_performance_user(self, login_page):
        login_page.open()
        login_page.login("performance_glitch_user", "secret_sauce")

        assert "inventory" in login_page.current_url
        assert login_page.is_inventory_visible()
