import allure
import  pytest
class  Test():
    @allure.step("执行登录操作")
    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def hello(self):
        allure.attach("描述:","输入用户名")
        allure.attach("描述:", "输入密码")
        allure.attach("描述:", "点击登录")
        print("登录操作")


    @allure.step("执行登录操作")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)

    def word(self):
        print("退出操作")
