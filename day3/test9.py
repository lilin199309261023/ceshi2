from time import sleep

from appium import webdriver

# server 启动参数
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# 输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.implicitly_wait(20)

"""
目标:move_to移动方法
需求:1.进入设置
    2.向上滑动屏幕到可见"安全"选线
    3.进入到安全
    4.点击屏幕锁定方式
    5.点击图案
    6.绘制图案
    
    踩得坑:
    1.元素等待必须有
    2.坐标点不是元素,必须添加sleep
"""
# 定位电池
dianchi=driver.find_element_by_xpath("//*[@text='电池']")
# 定位wlan
wlan=driver.find_element_by_xpath("//*[@text='WLAN']")
# 点击安全
driver.find_element_by_xpath("//*[@text='安全']").click()

# 点击屏幕锁定方式
driver.find_element_by_xpath("//*[@text='屏幕锁屏方式']").click()
# 点击安全
driver.find_element_by_xpath("//*[@text='图案']").click()
#后面坐标点减前面的坐标点
# A:x=234,y=857    x=722,y=857  x=1206,y=857
#B:x=857,y=1329
#C:x=234,y=1818  x=722,y=1818  x=1206,y=1818
TouchAction(driver).press(x=234,y=857).wait(100).move_to(x=722-857,y=0).wait(100).\
    move_to(x=1206-722,y=0).wait(100).move_to(x=722-1206,y=1329-857).wait(100).\
    move_to(x=234-722,y=1818-1329).wait(100).move_to(x=857-234,y=0).wait(100).move_to(x=1206-857,y=0).\
    wait(100).release().perform()



sleep(2)
driver.quit()







