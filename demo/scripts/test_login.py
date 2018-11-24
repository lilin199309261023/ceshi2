import os,sys
# 位置
sys.path.append(os.getcwd())

import pytest
"""项目名在子目录名文件名导入类名"""
from demo.base.get_driver import get_driver
from demo.page.page_login import Pagelogin

class Testlogin():
    # 初始化方法
    def setup_class(self):
        self.login=Pagelogin(get_driver())
    #     结束方法
    def teardown_class(self):
        # 关闭驱动对象
        self.login.driver.quit()
    # 测试方法
    def test_login(self,username='111111111',pwd='22222222222'):
    # 输入用户名
        self.login.page_input_username(username)
    # 输入密码
        self.login.page_input_password(pwd)
#     # 点击登陆
        self.login.page_click_login_btn()
if __name__ == '__main__':
    pytest.mian("-s test_login.py")

