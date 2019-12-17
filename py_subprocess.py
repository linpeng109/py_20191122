import multiprocessing
import sys


def fun(i):
    print(sys.path)
    print(sys.version_info)
    print(sys.platform)


if __name__ == '__main__':
    process = multiprocessing.Process(target=fun, args=(10, multiprocessing.queues.Queue))
    process.join()
    process.start()
