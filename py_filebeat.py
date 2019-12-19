import datetime
import py_logging

import psutil
from apscheduler.schedulers.blocking import BlockingScheduler


py_logging.basicConfig(filename='app.log', level=py_logging.DEBUG)


def MonitorSystem(logging=py_logging):
    cpuinfo = psutil.cpu_percent()
    meminfo = psutil.virtual_memory()
    now = datetime.datetime.now()
    timeinfo = now.strftime('%Y-%m-%D %H:%M:%S')
    line = f'{timeinfo} cpu:{cpuinfo} mem:{meminfo}'
    if (logging):
        logging.debug(line)
    else:
        print(line)


def MonitorNetWork(logging=py_logging):
    netinfo = psutil.net_io_counters()
    line = f'bytessent:{netinfo.bytes_sent} bytesrecv:{netinfo.bytes_recv}'
    if (logging):
        logging.debug(line)
    else:
        print(line)


def dojob():
    scheduler = BlockingScheduler()
    scheduler.add_job(MonitorSystem, 'interval', seconds=3, id='MonitorSystem')
    scheduler.add_job(MonitorNetWork, 'interval', seconds=2, id='MonitorNetWork')
    scheduler.start()


while True:
    dojob()
