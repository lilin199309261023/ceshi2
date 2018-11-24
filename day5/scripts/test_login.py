import pytest
from Base.get_driver import get_driver
from page.page1 import page1
class Testlogin():
    def setup_class(self):
        self.login=page1(get_driver())
    def teardown_class(self):
        self.login.driver.qiut()
    def test_login(self,username="1111111111",password="12545353"):
        self.login.page_username(username)
        self.login.page_input_password(password)
        self.login.page_click_login_tun()
if __name__ == '__main__':
    pytest.main("-s test_login.py")            