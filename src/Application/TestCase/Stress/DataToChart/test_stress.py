import pytest
import allure
import Infrastructure.Data.DailyDataRepository as daily
import Application.TestCase.Stress.DataToChart.Impl as Impl


@pytest.mark.usefixtures('init_module')
@allure.feature("数据图表_压力测试")
@pytest.mark.Test_Type_Stress
class TestStress:

    @allure.story("折线画图 性能测试")
    @pytest.mark.DataToChart_Version_1015
    def test_linechart(self, init_module):
        code = "USHA600000"
        version = "1.0.0"
        guid = "{E50AB1DF-AAE3-48BA-8819-D3802405F35D}"
        pid = init_module

        recoverTestData = daily.GetTestData(code, 1, "Open")
        processTestData = daily.GetTestData(code, 5, "Open")

        stress = Impl.StressImpl()
        stress.Execute(5, pid, guid, version, code,
                       recoverTestData, processTestData)
