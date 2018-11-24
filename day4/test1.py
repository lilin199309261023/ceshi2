import pytest


class Test1():
    def test_hello(self):
        print("hello被执行")
    def test_word(self):
        print("word被执行")

        #以下运行方式 只是作为调试使用
if __name__ == '__main__':
     pytest.main("-s test1.py")
