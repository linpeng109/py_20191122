import multiprocessing
import os


def run_pro(name):
    print('Child Process {0}  {1} Running'.format(name, os.getpid()))


if __name__ == "__main__":
    for i in range(5):
        p = multiprocessing.Process(target=run_pro, args=(str(i)))
        p.start()
    # p.join()
    print('Process closed')
