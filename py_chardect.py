import chardet


def dectect(filename):
    file = open(filename, 'rb')
    data = file.read()
    return chardet.detect(data)


if __name__ == '__main__':
    # filename = '20191127HCS.txt'
    filename = '20191127AAS.txt'
    result = dectect(filename=filename)
    print(result)
