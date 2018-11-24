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


"""
目标:模拟手势高级操作--轻敲
需求:1.打开设置
    2.轻敲wlan(无线wifi)
"""
# #定位wlan

wlan=driver.find_element_by_xpath("//*[@text='WLAN']")
# 基于元素轻敲
#TouchAction(driver).tap(wlan).press()

# 注:TouchAction类中,所有的方法都必须执行perform()fangfa 方法才能执行!
# 基于坐标轻敲
TouchAction(driver).tap(x=395,y=645).perform()




sleep(2)
driver.quit()







