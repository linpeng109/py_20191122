import logging
import time

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

import py_config

cfg = py_config.getCfg('py_watchdog.ini')


def on_created(event):
    print(event.src_path)


def createObserver():
    print("WatchDog has started.")
    time.sleep(1)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = PatternMatchingEventHandler(patterns=cfg.options('parrents'),
                                                ignore_directories=True,
                                                case_sensitive=False)
    event_handler.on_created = on_created
    observer = Observer()
    observer.schedule(event_handler, cfg.get('watchdog', 'watchpath'),
                      recursive=cfg.getboolean('watchdog', 'recursive'))
    observer.start()
    return observer


if __name__ == "__main__":
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    observer = createObserver()
    try:
        while observer.is_alive():
            observer.join(1)
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
        print("WatchDog had stopped.")
    observer.join()
