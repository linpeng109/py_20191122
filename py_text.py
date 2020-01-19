import numpy as np


def readText(textFileName):
    textFile = open(textFileName, 'r', encoding='utf-16', errors='ignore')
    lines = textFile.readlines()
    dataArray = []
    for line in lines:
        num = list(map(str, line.strip('\n').split('\t')))
        # num = line \
        #     .strip('\n') \
        #     .split('\t')
        dataArray.append(num)

    dataArray = np.delete(dataArray, [0, 1], axis=0)
    # dataArray = np.delete(dataArray, 1, 1)
    dataArray = np.sort(dataArray, axis=0)
    print(dataArray)
    np.savetxt("a.csv", dataArray, encoding='utf-16', delimiter=",", fmt='%s')
    textFile.close()


if __name__ == '__main__':
    textFileName = "20191127HCS.txt"
    readText(textFileName=textFileName)
