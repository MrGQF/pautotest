import os
import psutil
import pandas as pd
from PyQt5.QtWidgets import QApplication
import Infrastructure.Analysis.ImageSimilarity as ImageSimilarity
import sys
import matplotlib.pyplot as plt
plt.style.use("seaborn-darkgrid")


def GetCpuTime(pid):
    p = psutil.Process(pid)
    cpu_times = 0
    for item in p.cpu_times():
        cpu_times += item
    return cpu_times


def GetMemoryPercent(pid):
    p = psutil.Process(pid)
    return p.memory_percent()


def SaveWidgetProfile(filePath, index, mem_percent, cpu_time, similarity):
    dataframe = pd.DataFrame(
        {'index': index, 'mem_percent': mem_percent, "cpu_time": cpu_time, "similarity": similarity})

    dataframe.to_csv(filePath, index=False, sep=',')


def ShowProfile(filePath):
    data = pd.read_csv(filePath)
    xdata = data.loc[:, "index"]
    y1data = data.loc[:, 'cpu_time']
    y2data = data.loc[:, 'mem_percent']
    y3data = data.loc[:, 'similarity']
    plt.plot(xdata, y1data, color='r', marker='o',
             mec='r', mfc='w', label=u'cpu_time')
    plt.plot(xdata, y2data, color='b', marker='o',
             mec='r', mfc='w', label=u'mem_percent')
    plt.plot(xdata, y3data, color='y', marker='o',
             mec='r', mfc='w', label=u'similarity')
    plt.title(u"Profile", size=10)
    plt.legend()
    plt.xlabel(u'Index', size=10)
    plt.ylabel(u'Metric', size=10)
    plt.show()


def DiffPicture(reference, compare):
    return ImageSimilarity.DiffPicture(reference, compare)


def SaveWindowPicture(widgetHandle, path):
    _ = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(widgetHandle).toImage()
    img.save(path)


if __name__ == "__main__":
    path = os.path.abspath("./src/Application/TestResult/E50AB1DF-AAE3-48BA-8819-D3802405F35D/TestStress.csv")
    ShowProfile(path)
