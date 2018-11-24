
from selenium.webdriver.common.by import By
from Base.base import Base


# loc为元组,值没有括号pycharm都可以识别为元组,注:无括号时两个值以上为元组
loc_usname= (By.ID, "com.vcooline.aike:id/etxt_username")
loc_pwd=(By.ID, "com.vcooline.aike:id/etxt_pwd")
loc_btn=(By.ID, "com.vcooline.aike:id/btn_login")

class Pagelogin(Base):
    """
    page页面思路:
    1.一个页面一个对象
    2.对象页面内需要操作的步骤,每一个步骤单独封装一个方法
    """
    #输入用户名
    def page_usname(self,text):
        # 调用base类 封装的输入方法,继承base,直接通过self.xxx
        self.base_input(loc_usname,text)
    #输入密码
    def page_password(self,text):
        self.base_input(loc_pwd,text)
    #     点击登录
    def page_btu(self):
        self.base_click(loc_btn)


# com.vcooline.aike /.umanager.LoginActivity