from configparser import ConfigParser

cfg = ConfigParser()
cfg.read(filenames='config.ini', encoding='utf8')

if __name__ == '__main__':
    print(cfg.sections())
    print(cfg.getint('default', 'port').__class__)
    print(cfg.get('default', 'port'))
