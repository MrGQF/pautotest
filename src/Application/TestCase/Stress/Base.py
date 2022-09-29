import abc
import os
import Infrastructure.Analysis.Profile as Profile
import Application.Sdk.Invoke.WidgetProcessor as WidgetProcessor
import time


class StressProcessor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Init(self, widgetHandle, param):  # 初始化
        pass

    @abc.abstractmethod
    def Recover(self, widgetHandle, param):  # 复原
        pass

    @abc.abstractmethod
    def Process(self, widgetHandle, param):  # 构建
        pass

    def Execute(self, loop, pid, widgetGuid, widgetVersion,  initParam, recoverParam, processParam):  # 测试执行

        filePathPre = os.path.abspath("./src/Application/TestResult/" + str(
            widgetGuid.replace("{", "").replace("}", "")) + "/TestStress")

        value = WidgetProcessor.Create(
            widgetGuid, widgetVersion, "Visible", "Visible")
        widgetHandle = value.WidgetHandle

        self.Init(widgetHandle, initParam)

        self.Recover(widgetHandle, recoverParam)

        CpuTimes = []
        MemPercent = []
        Index = []
        Similarity = []
        for i in range(loop):
            self.Recover(widgetHandle, recoverParam)

            cputime_Default = Profile.GetCpuTime(pid)
            time.sleep(1)

            self.Process(widgetHandle, processParam)
            cputime_SetData = Profile.GetCpuTime(pid) - cputime_Default
            CpuTimes.append(cputime_SetData)
            MemPercent.append(Profile.GetMemoryPercent(pid))
            time.sleep(1)
            Index.append(i)

            resultPicPath = filePathPre + str(i) + ".png"
            Profile.SaveWindowPicture(int(widgetHandle), resultPicPath)
            Similarity.append(Profile.DiffPicture(
                filePathPre + ".png", resultPicPath))

        Profile.SaveWidgetProfile(
            filePath=filePathPre + ".csv", index=Index, mem_percent=MemPercent, cpu_time=CpuTimes, similarity=Similarity)

        WidgetProcessor.Close()


if __name__ == "__main__":
    filePathPre = os.path.join(
        "./src/Application/TestResult", "chart") + "/Test.png"
    print(os.path.abspath(filePathPre))

    path2 = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    print(path2)
