import sys
import time

import servicemanager
import win32.win32event as win32event
import win32.win32service as win32service
import win32serviceutil


class PythonService(win32serviceutil.ServiceFramework):
    # 服务名
    _svc_name_ = "PythonService"
    # 服务显示名称
    _svc_display_name_ = "PythonServiceTest"
    # 服务描述
    _svc_description_ = "Python Service Test"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.run = True

    def SvcDoRun(self):
        # print("服务启动......")
        while self.run:
            self._Log('start')
            time.sleep(7)

    def SvcStop(self):
        # print("服务停止......")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.run = False
        self._Log('stop')

    def _Log(self, str):
        with open('D:/helloServices.txt', 'a') as f:
            f.writelines('hello world' + str + '\n')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(PythonService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(PythonService)
