from day5.base.test1 import Base


class Page(Base):
    # 点击搜索按钮
    def page_click_search_btn(self):
        self.base_click_element()
    #     搜索框内输入内容
    def papg_click_search(self,value):
        self.base_find_element(input_text,value)
    #     点击返回
    def page_click_back(self):
        self.base_click_element()
