import pytest


class Test():
    @pytest.mark.skipit(1 > 0, reason="条件成立,方法跳过")
    def setup_class(self):
        print("新增")
    @pytest.mark.xfail(1>0,reason="条件成立,预期失败")
    def teardown_class(self):
        print("修改")

    def test_a(self):
        print("查看")

    def test_b(self):
        print("删除")

