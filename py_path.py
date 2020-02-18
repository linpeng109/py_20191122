import os.path
import os


def splitFullPathFileName(fullPathFileName):
    driver = os.path.splitdrive(fullPathFileName)[0]
    path = os.path.split(fullPathFileName)[0]
    filename = os.path.split(fullPathFileName)[1]
    ext = os.path.splitext(fullPathFileName)[1]
    main = filename.strip(ext)
    sep = os.sep
    return {'driver': driver, 'sep': os.sep, 'path': path, 'filename': filename, 'main': main, 'ext': ext}


def filenameIsContains(fullPathFileName, strs):
    filename = splitFullPathFileName(fullPathFileName).get('filename')
    result = True
    for str in strs:
        result = filename.__contains__(str) and result
    return result


if __name__ == '__main__':
    fullname = '/home/pi/Shared/AFS-8510.xlsx'
    result1 = splitFullPathFileName(fullname)
    print(result1)
    result = filenameIsContains(fullname, ['AFS', 'xlsx'])
    print(result)
