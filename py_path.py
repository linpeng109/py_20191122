import os
import os.path


def splitFullPathFileName(fullPathFileName):
    fullPathFileName = fullPathFileName.lower()
    driver = os.path.splitdrive(fullPathFileName)[0]
    path = os.path.split(fullPathFileName)[0]
    filename = os.path.split(fullPathFileName)[1]
    ext = os.path.splitext(fullPathFileName)[1]
    main = filename.strip(ext)
    sep = os.sep
    return {'driver': driver, 'sep': os.sep, 'path': path, 'filename': filename, 'main': main, 'ext': ext}


def filenameIsContains(fullPathFileName, strs):
    filename = splitFullPathFileName(fullPathFileName).get('filename').lower()
    result = True
    for str in strs:
        result = filename.__contains__(str.lower()) and result
    return result


def outpathIsExist(outputPath):
    isExist = os.path.isdir(outputPath)
    if not isExist:
        os.makedirs(outputPath)
        print('The Path is not exist. I have make it.')
    else:
        print('The path is exit')


if __name__ == '__main__':
    # fullname = '/home/pi/Shared/AFS-8510.xlsx'
    # result1 = splitFullPathFileName(fullname)
    # print(result1)
    # result = filenameIsContains(fullname, ['AFS', 'xlsx'])
    # print(result)
    outpathIsExist('e:/watchdogdir/aass')
