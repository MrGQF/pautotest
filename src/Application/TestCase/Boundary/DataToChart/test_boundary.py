import allure
import pytest
from Application.TestData import DataManager as Data


@allure.feature("数据图表_边界测试")
@pytest.mark.Test_Type_Boundary
class TestBoundary:

    # pytest src -m "Test_Mark--alluredir  ./Allure/result/Test_Mark "
    @allure.story("测试数据")
    @allure.link("www.baidu.com", "测试报告")
    @pytest.mark.Test_Mark
    @pytest.mark.parametrize("a, b, result", Data.Read())
    def test_demo(self, a, b, result):
        allure.attach("结果", result)
        assert a + b == result
