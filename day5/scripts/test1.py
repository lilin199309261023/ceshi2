from selenium.webdriver.common.by import By
loc=(By.XPATH,'//*[contains(@text,"WALN")]')
print(type(loc))
print(loc)
print("解包后的值:",*loc)