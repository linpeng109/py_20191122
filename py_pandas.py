from multiprocessing import Process

import pandas as pd
import py_config
import py_logging
import py_path as path
# import py_wx as wx
import winsound

cfg = py_config.getCfg(config='py_watchdog.ini')
logger = py_logging.getLogger(config='py_watchdog.ini')


def convertHCSTxt(hcsTextFileName):
    # 读取
    dict = {'sep': ' ', 'encoding': 'UTF-16', 'dtype': 'str', 'header': None, 'engine': 'python', 'na_filter': False}
    hcsDf = pd.read_csv(filepath_or_buffer=hcsTextFileName, **dict)
    logger.debug(hcsDf)
    # 处理清洗
    hcsDf = hcsDf.drop(index=[0, 1])  # 删除表头标题
    # print(hcsDf)
    logger.debug(hcsDf)
    # 排序
    hcsDf = hcsDf.sort_index(0, ascending=False)
    # hcsDf = hcsDf.dropna()
    logger.debug(hcsDf)
    # 写入文本
    newfilename = convertFilename(hcsTextFileName)
    # hcsDf.to_csv(newfilename, index=None, header=None)
    logger.debug(newfilename)
    hcsDf.to_csv(newfilename, index=None, header=None, encoding='gbk', line_terminator='\r\n')
    return hcsDf


def convertAFSExcel(afsExcelFileName):
    # 读取
    dict = {'sheet_name': '样品测量数据', 'header': None}
    afsDf = pd.read_excel(afsExcelFileName, **dict)
    logger.debug(afsDf)
    # 处理清洗
    afsDf = afsDf.drop(index=[0, 1, 2])
    logger.debug(afsDf)
    # 写入文本
    newfilename = convertFilename(afsExcelFileName)
    afsDf.to_csv(newfilename, index=None, header=None, encoding='gbk', line_terminator='\r\n')


def convertAASTxt(aasTextFilename):
    # 读取
    dict = {'dtype': 'str',
            'header': None, 'engine': 'python'}
    aasDf = pd.read_csv(filepath_or_buffer=aasTextFilename, encoding='gbk', **dict)
    # 写入文本
    newfilename = convertFilename(aasTextFilename)
    aasDf.to_csv(newfilename, index=None, header=None, encoding='gbk', line_terminator='\r\n')
    return aasDf


def convertFilename(filename):
    outpath = 'd:/'
    fileinfo = path.splitFullPathFileName(filename)
    newfilename = (fileinfo.get('path') + fileinfo.get('sep') + fileinfo.get('main') + '_OK' + '.txt')
    return newfilename



def startProcess(file):
    winsound.Beep(500, 300)
    if (path.filenameIsContains(file, ['AAS.txt'])):
        process = Process(target=convertAASTxt, args=(file,))
        process.start()
    if (path.filenameIsContains(file, ['HCS.txt'])):
        process = Process(target=convertHCSTxt, args=(file,))
        process.start()
    if (path.filenameIsContains(file, ['AFS', '.xlsx'])):
        process = Process(target=convertAFSExcel, args=(file,))
        process.start()
    # if (path.filenameIsContains(file, ['puid.txt'])):
    #     process = Process(target=convertPUID, args=(file,))
    #     process.start()

if __name__ == '__main__':
    aasTextFileName = '20191127AAS.txt'
    p = Process(target=convertAASTxt, args=(aasTextFileName,))
    p.start()
