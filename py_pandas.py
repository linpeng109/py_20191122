# import py_wx as wx
from multiprocessing import Process

import pandas as pd

import py_config
import py_path as path
import py_qrcode as qrcode

_cfg = py_config.getCfg(config='py_watchdog.ini')


# _log = object


def _getNewFilename(filename, type='default'):
    newpath = _cfg.get(type, 'outpath')
    path.outpathIsExist(newpath)
    fileinfo = path.splitFullPathFileName(filename)
    newfilename = (newpath + fileinfo.get('sep') + fileinfo.get('main') + '_OK' + '.txt')
    return newfilename


def convertHCSTxt(hcsTextFileName):
    dict = {'sep': ' ', 'encoding': 'UTF-16', 'dtype': 'str', 'header': None, 'engine': 'python', 'na_filter': False}
    hcsDf = pd.read_csv(filepath_or_buffer=hcsTextFileName, **dict)
    # print(hcsDf)
    hcsDf = hcsDf.drop(index=[0, 1])  # 删除表标题
    # print(hcsDf)
    # 排序
    hcsDf = hcsDf.sort_index(0, ascending=False)
    # print(hcsDf)
    # _log.debut(hcsDf)
    newfilename = _getNewFilename(hcsTextFileName, 'hcs')
    print(newfilename)
    encoding = _cfg.get('hcs', 'encoding')
    hcsDf.to_csv(newfilename, index=None, header=None, encoding=encoding, line_terminator='\r\n')
    return hcsDf


def convertHCSExcel(hcsExcelFileName):
    dict = {'sheet_name': 0, 'header': None}
    hcsDf = pd.read_excel(hcsExcelFileName, **dict)
    # print(hcsDf)
    hcsDf = hcsDf.drop(index=[0, 1])  # 删除表标题
    print(hcsDf)
    newfilename = _getNewFilename(hcsExcelFileName, 'hcs')
    encoding = _cfg.get('hcs', 'encoding')
    hcsDf.to_csv(newfilename, index=None, header=None, encoding=encoding, line_terminator='\r\n')


def convertAFSExcel(afsExcelFileName):
    dict = {'sheet_name': '样品测量数据', 'header': None}
    afsDf = pd.read_excel(afsExcelFileName, **dict)
    # print(afsDf)
    afsDf = afsDf.drop(index=[0, 1, 2])
    print(afsDf)
    newfilename = _getNewFilename(afsExcelFileName, 'afs')
    encoding = _cfg.get('afs', 'encoding')
    afsDf.to_csv(newfilename, index=None, header=None, encoding=encoding, line_terminator='\r\n')


def convertAASTxt(aasTextFilename):
    dict = {'dtype': 'str',
            'header': None, 'engine': 'python'}
    aasDf = pd.read_csv(filepath_or_buffer=aasTextFilename, encoding='gbk', **dict)
    print(aasDf)
    newfilename = _getNewFilename(aasTextFilename, 'aas')
    encoding = _cfg.get('aas', 'encoding')
    aasDf.to_csv(newfilename, index=None, header=None, encoding=encoding, line_terminator='\r\n')
    return aasDf


def convertPUID(puidFilename):
    data = "http://192.168.1.104:8822/download"
    img = qrcode.getQRCode(data=data)
    img.show()


def startProcess(event):
    file = event.src_path
    if (path.filenameIsContains(file, ['AAS.txt'])):
        process = Process(target=convertAASTxt(file), args=(file,))
    elif (path.filenameIsContains(file, ['HCS', '.xls'])):
        process = Process(target=convertHCSExcel(file), args=(file,))
    elif (path.filenameIsContains(file, ['HCS.txt'])):
        process = Process(target=convertHCSTxt(file), args=(file,))
    elif (path.filenameIsContains(file, ['AFS', '.xlsx'])):
        process = Process(target=convertAFSExcel(file), args=(file,))
    elif (path.filenameIsContains(file, ['puid.txt'])):
        process = Process(target=convertPUID(file), args=(file,))

    process.start()
    process.join(timeout=10000)


if __name__ == '__main__':
    aasTextFileName = '20191127AAS.txt'
    p = Process(target=convertAASTxt, args=(aasTextFileName,))
    p.start()
