from configparser import ConfigParser


class _Configparser(ConfigParser):
    def optionxform(self, optionstr):
        return optionstr


def getCfg(config):
    cfg = _Configparser()
    cfg.read(filenames=config, encoding='utf8')
    return cfg


if __name__ == '__main__':
    cfg = getCfg('py_watchdog.ini')
    dic = dict(cfg.items('logger'))
    print(dic)
