import pytest


class Test():

    def setup_class(self):
        print("setup_class被执行")
    def teardown_class(self):
        print("teardown_class被执行")
    def teardown(self):
        print("teardown被执行")
    def setup(self):
        print("setup被执行")
    def test1(self):
        print("test1被执行")
if __name__ == '__main__':
    pytest.main("-s test2.py")
