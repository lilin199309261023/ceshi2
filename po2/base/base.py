class Base():


    def __init__(self,driver):
        self.driver1=driver

    #     获取元素
    def base_login(self,loc):
        el=self.driver1.find_element(*loc)
#       返回元素
    
