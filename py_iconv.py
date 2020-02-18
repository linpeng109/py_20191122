import subprocess
import chardet


# only for Linux System
# convert
def chardetect(inputfile):
    file = open(inputfile, mode='rb')
    stream = file.read()
    result = chardet.detect(stream)
    file.close()
    return result


def iconv(fro, to, inputfile, outputfile):
    cmd = r'iconv -f ' + fro + ' -t ' + to + ' -o ' + outputfile + ' ' + inputfile
    print(cmd)
    p = subprocess.Popen(args=cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.wait()
    return {'stdout': p.stdout.readlines(), 'stderror': p.stderr.readlines()}
    # result = subprocess.check_output(cmd).decode('utf-8')
    # return result


def todos(inputfile):
    cmd = 'todos -u ' + inputfile
    print(cmd)
    p = subprocess.Popen(args=cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.wait()
    return {'stdout': p.stdout.readlines(), 'stderror': p.stderr.readlines()}


if __name__ == '__main__':
    # inputfile = '/home/pi/Shared/20191127HCS_OK.txt'
    # outputfile = '/home/pi/Shared/ansi.txt'
    # fro = 'utf-8'
    # to = 'gbk'
    # print(iconv(inputfile=inputfile, outputfile=outputfile, fro=fro, to=to))

    inputfile = '/home/pi/Shared/ansi.txt'
    print(todos(inputfile=inputfile))

    # inputfile = '/home/pi/Shared/ansi.txt'
    # print(chardetect(inputfile=inputfile).get('encoding'))
