import numpy as np


def main(textfilename):
    # lines = np.loadtxt(textfilename, dtype='str', skiprows=3, encoding='utf-16')
    lines = np.genfromtxt(textfilename, delimiter=' ', skip_header=3, dtype='str', encoding='utf-16')
    # lines = np.loadtxt(textfilename, delimiter='  ', dtype='str', encoding='utf-16', unpack=True, skiprows=2)
    print(type(lines))



if __name__ == '__main__':
    main(textfilename='20191127HCS.txt')
