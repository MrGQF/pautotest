import abc
import os
import profile
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

        loadtimes = []
        indexs = []
        similaritys = []
        cpu_percents = []
        mems = []
        num_handles = []
        num_threads = []
        gdi_objs = []
        io_readcounts = []
        io_writecounts = []
        for i in range(loop):
            self.Recover(widgetHandle, recoverParam)

            cputime_before = Profile.GetCpuTime(pid)
            time.sleep(1)

            self.Process(widgetHandle, processParam)

            cputime_after = Profile.GetCpuTime(pid)
            loadtime = cputime_after - cputime_before
            loadtimes.append(loadtime)

            tuple = Profile.GetIndexs(pid)
            mems.append(tuple["mem"])
            cpu_percents.append(tuple["cpu_percent"])
            num_handles.append(tuple["num_handle"])
            num_threads.append(tuple["num_thread"])
            gdi_objs.append(tuple["gdi_obj"])
            io_readcounts.append(tuple["io_readcount"])
            io_writecounts.append(tuple["io_writecount"])
            indexs.append(i)

            resultPicPath = filePathPre + str(i) + ".png"
            Profile.SaveWindowPicture(int(widgetHandle), resultPicPath)
            similarity = Profile.DiffPicture(
                filePathPre + ".png", resultPicPath)
            similaritys.append(similarity)

        Profile.SaveWidgetProfile(
            filePath=filePathPre + ".csv",
            indexs=indexs,
            loadtimes=loadtimes,
            similaritys=similaritys, cpu_percents=cpu_percents,
            mems=mems,
            num_handles=num_handles,
            num_threads=num_threads,
            gdi_objs=gdi_objs,
            io_readcounts=io_readcounts,
            io_writecounts=io_writecounts)

        WidgetProcessor.Close()


if __name__ == "__main__":
    filePathPre = os.path.join(
        "./src/Application/TestResult", "chart") + "/Test.png"
    print(os.path.abspath(filePathPre))

    path2 = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    print(path2)
