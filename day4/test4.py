import pytest

class Test():
    def setup_class(self):
        print("新增")

    def teardown_class(self):
        print("修改")

    def test_a(self):
        print("查看")

    def test_b(self):
        print("删除")

