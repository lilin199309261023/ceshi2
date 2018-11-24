import pytest


class Test():
    @pytest.mark.run(order=1)
    def setup_class(self):
        print("新增")

    @pytest.mark.run(order=2)
    def teardown_class(self):
        print("修改")

    @pytest.mark.run(order=3)
    def test_a(self):
        print("查看")

    @pytest.mark.run(order=4)
    def test_b(self):
        print("删除")

