#encodeing:utf-8
import csv
import os
import re
import sys
import matplotlib.pyplot as plt
import numpy as np

mData = []
#湿敏电阻文件解析
def handHygristor(filename):
    #csv_ThResistor = csv.reader(open(filename,'r'))
    data = []
    with open(filename) as f:
        csv_ThResistor = csv.reader(f)
        print(csv_ThResistor)
        for line in csv_ThResistor:
            for i in range(0,len(line)):
               # print(type(line[i]))
                j = line[i].find('K')
                k = line[i].find('M')
                if j != -1:
                    s = line[i]
                    d = float(s[0:j]) * 1000
                elif k != -1:
                    tmp = line[i]
                    s2 = float(tmp[0:k])
                    d = s2 * 1000000
                else:
                    d = line[i]
                data.append(str(d))
            mData.append(data)
            data = []
        print (mData)
            
                
#热敏电阻文件解析
def handThermalResistor(filename):
    # csv_ThResistor = csv.reader(open(filename,'r'))
    first = True
    with open(filename) as f:
        csv_ThResistor = csv.reader(f)
        print(csv_ThResistor)
        for line in csv_ThResistor:
            print(len(line))
            print(line)


def write(path, filename):
    s = ''
    if not os.path.exists(path):
        os.mkdir(path)
    with open("tmp", "w") as fb:
        for data in mData:
            s = data[0]
            for div in data[1:]:
                s = s + "," + div
            s = s + "\n"
            fb.write(s)
        fb.flush()
    if os.path.exists(os.path.join(path, filename + ".old")):
        os.remove(os.path.join(path, filename + ".old"))
    if os.path.exists(os.path.join(path, filename)):
        os.rename(os.path.join(path, filename), os.path.join(path, filename + ".old"))
    os.rename('tmp', os.path.join(path, filename))


if __name__ == '__main__':
    ThermaResistorfilename = "热敏电阻.csv"
    hygristorFilename = "湿敏电阻.csv"
    INPUTPATH = "./" + hygristorFilename
    handHygristor(INPUTPATH)
    write('./', "humidity.csv")


