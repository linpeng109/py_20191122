from multiprocessing import Process

import pandas as pd

import py_path as path


def convertHCSTxt(hcsTextFileName):
    # 读取
    # dict = {'sep': ' ', 'encoding': 'UTF-16', 'dtype': 'str', 'header': None, 'engine': 'python'}
    dict = {'sep': ' ', 'encoding': 'UTF-16', 'dtype': 'str', 'header': None, 'engine': 'python', 'na_filter': True}
    hcsDf = pd.read_csv(filepath_or_buffer=hcsTextFileName, **dict)
    print(hcsDf)
    # 处理清洗
    print('=========== dropna ==============')
    hcsDf.dropna(axis=1, how='all', inplace=False)
    # hcsDf = hcsDf.drop(index=[0, 1])  # 删除表头标题
    # print(hcsDf)
    print(hcsDf)
    # hcsDf = hcsDf.sort_index(0, ascending=False)
    # print(hcsDf)
    # 写入文本
    # newfilename = convertFilename(hcsTextFileName)
    # hcsDf.to_csv(newfilename, index=None, header=None)
    # hcsDf.to_csv(newfilename, index=None, header=None, encoding='gbk', line_terminator='\r\n')
    return hcsDf


def convertAFSExcel(afsExcelFileName):
    # 读取
    dict = {'sheet_name': '样品测量数据', 'header': None}
    afsDf = pd.read_excel(afsExcelFileName, **dict)
    print(afsDf)
    # 处理清洗
    afsDf = afsDf.drop(index=[0, 1, 2])
    print(afsDf)
    # 写入文本
    newfilename = convertFilename(afsExcelFileName)
    afsDf.to_csv(newfilename, index=None, header=None, encoding='gbk', line_terminator='\r\n')


def convertAASTxt(aasTextFilename):
    # 读取
    dict = {'dtype': 'str',
            'header': None, 'engine': 'python'}
    aasDf = pd.read_csv(filepath_or_buffer=aasTextFilename, encoding='GB2312', **dict)
    # 写入文本
    newfilename = convertFilename(aasTextFilename)
    aasDf.to_csv(newfilename, index=None, header=None, encoding='gbk', line_terminator='\r\n')
    return aasDf


def convertFilename(filename):
    fileinfo = path.splitFullPathFileName(filename)
    newfilename = (fileinfo.get('path') + fileinfo.get('sep') + fileinfo.get('main') + '_OK' + '.txt')
    return newfilename


def startProcess(file):
    if (path.filenameIsContains(file, ['AAS.txt'])):
        process = Process(target=convertAASTxt, args=(file,))
        process.start()
    if (path.filenameIsContains(file, ['HCS.txt'])):
        process = Process(target=convertHCSTxt, args=(file,))
        process.start()
    if (path.filenameIsContains(file, ['AFS', '.xlsx'])):
        process = Process(target=convertAFSExcel, args=(file,))
        process.start()


if __name__ == '__main__':
    aasTextFileName = '20191127AAS.txt'
    p = Process(target=convertAASTxt, args=(aasTextFileName,))
    p.start()
