import os
import psutil
import pandas as pd
from PyQt5.QtWidgets import QApplication
import Infrastructure.Analysis.ImageSimilarity as ImageSimilarity
import sys
from ctypes import windll


def GetCpuTime(pid):
    p = psutil.Process(pid)
    cpu_times = 0
    for item in p.cpu_times():
        cpu_times += item
    return cpu_times


def GetIndexs(pid):
    p = psutil.Process(pid)
    cpu_percent = p.cpu_percent()

    mem = p.memory_info().rss / 1024

    num_handles = p.num_handles()

    num_threads = p.num_threads()

    gdi_obj = 0
    PH = windll.kernel32.OpenProcess(0x400, 0, pid)
    gdi_obj = windll.user32.GetGuiResources(PH, 0)
    windll.kernel32.CloseHandle(PH)

    io_readcount = p.io_counters().read_count

    io_writecount = p.io_counters().write_count
    return {
        "cpu_percent": cpu_percent,
        "mem": mem,
        "num_handle": num_handles,
        "num_thread": num_threads,
        "gdi_obj": gdi_obj,
        "io_readcount": io_readcount,
        "io_writecount": io_writecount
    }


def SaveWidgetProfile(
        filePath,
        indexs,
        loadtimes,
        similaritys,
        cpu_percents,
        mems,
        num_handles,
        num_threads,
        gdi_objs,
        io_readcounts,
        io_writecounts):
    dataframe = pd.DataFrame(
        {'index': indexs,
         "loadtime": loadtimes,
         "similarity": similaritys,
         "cpu_percent": cpu_percents,
         "mem": mems,
         "num_handles": num_handles,
         "num_threads": num_threads,
         "gdi_objs": gdi_objs,
         "io_readcounts": io_readcounts,
         "io_writecounts": io_writecounts})

    dataframe.to_csv(filePath, index=False, sep=',')


def DiffPicture(reference, compare):
    return ImageSimilarity.DiffPicture(reference, compare)


def SaveWindowPicture(widgetHandle, path):
    _ = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(widgetHandle).toImage()
    img.save(path)


if __name__ == "__main__":
    path = os.path.abspath(
        "./src/Application/TestResult/E50AB1DF-AAE3-48BA-8819-D3802405F35D/TestStress.csv")
