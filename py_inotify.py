import pyinotify

import py_config
import py_logging
import py_pandas as conv
import py_path as path


class EventHandler(pyinotify.ProcessEvent):
    logger = py_logging.getLogger()

    def process_IN_ACCESS(self, event):
        print("ACCESS event:", event.pathname)

    def process_IN_ATTRIB(self, event):
        print("ATTRIB event:", event.pathname)

    def process_IN_CLOSE_NOWRITE(self, event):
        print("CLOSE_NOWRITE event:", event.pathname)

    def process_IN_CLOSE_WRITE(self, event):
        file = event.pathname
        conv.startProcess(file)
        print("CLOSE_WRITE event:", event.pathname)

    def process_IN_CREATE(self, event):
        print("CREATE event:", event.pathname)

    def process_IN_DELETE(self, event):
        print("DELETE event:", event.pathname)

    def process_IN_MODIFY(self, event):
        print("MODIFY event:", event.pathname)

    def process_IN_OPEN(self, event):
        print("OPEN event:", event.pathname)


if __name__ == '__main__':
    cfg = py_config.getCfg()
    logger = py_logging.getLogger()
    wm = pyinotify.WatchManager()
    handler = EventHandler()
    notifier = pyinotify.Notifier(wm, handler)
    sharedDir = cfg.get('inotity', 'watch')
    logger.debug(sharedDir)
    wdd = wm.add_watch('/home/pi/Shared', pyinotify.IN_CLOSE_WRITE, rec=True)
    notifier.loop()
