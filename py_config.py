from configparser import ConfigParser


def getCfg(filename):
    cfg = ConfigParser()
    cfg.read(filenames=filename, encoding='utf8')
    return cfg


if __name__ == '__main__':
    cfg = getCfg('py_watchdog.ini')

    # print(cfg.sections())
    print(cfg.options('parrents'))
    print(cfg.get('watchdog','watchpath'))
    print(cfg.get('watchdog', 'recursive'))