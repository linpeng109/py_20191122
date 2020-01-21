import numpy as np


def main(textfilename):
    lines = np.loadtxt(textfilename, dtype='str', skiprows=3, encoding='utf-16')
    print(type(lines))


if __name__ == '__main__':
    main(textfilename='20191127HCS.txt')
