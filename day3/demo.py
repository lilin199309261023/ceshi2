# from appium import webdriver
# desired_caps = {}
# # 必填-且正确
# desired_caps['platformName'] = 'Android'
# # 必填-且正确
# desired_caps['platformVersion'] = '5.1'
# # 必填    只针对虚拟器192.168.56.101:5555
# desired_caps['deviceName'] = '192.168.35.101:5555'
# # APP包名
# desired_caps['appPackage'] = 'com.android.settings'
# # 启动名
# desired_caps['appActivity'] = '.Settings'
#
# webdriver.Remote('http://127.0.0.1:4723/wb/hub/',desired_caps)


from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = 'Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.find_element_by_id('com.android.dialer:id/search_box_collapsed').click()
# search_box = driver.find_element_by_id('com.android.dialer:id/search_view')
# search_box.click()
# search_box.send_keys('hello toby')
