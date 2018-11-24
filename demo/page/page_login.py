from selenium.webdriver.common.by import By

from demo.base.base import Base

loc_username = (By.ID, "com.vcooline.aike:id/etxt_username")
loc_pwd = By.ID, "com.vcooline.aike:id/etxt_pwd"
loc_login_btn = By.ID, "com.vcooline.aike:id/btn_login"

class Pagelogin(Base):
    # 输入用户名
    def page_input_username(self, text):
        self.base_input(loc_username,text)
    def page_input_password(self,text):
        # 调用base类  封装的输入方法  以为继承base 所以直接通过self.xxxx
        self.base_input(loc_pwd,text)
        # 点击登录
    def page_click_login_btn(self):
         self.base_click(loc_login_btn)
"""
page页面思路
1.一个页面一个对象(新建class)
2.对象页面内需要操作的步骤,每个步骤单独封装一个方法
"""