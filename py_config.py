from configparser import ConfigParser


def getCfg():
    cfg = ConfigParser()
    cfg.read(filenames='config.ini', encoding='utf8')
    return cfg


if __name__ == '__main__':
    cfg = getCfg()

    # print(cfg.sections())
    print(cfg.get('ftpd', 'port'))
    print(cfg.get('logging', 'filename'))
    print(cfg.get('ftpd', 'username'))
