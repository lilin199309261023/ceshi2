import pytest

@pytest.fixture(scope="module")
def before():
    return "hello"

class Test():
    def test_delete(self):
        print("删除")
    def test_get(self):
        print("查询")
    def test_put(self):
        print("修改")
    def test_post(self):
        print("新增")
