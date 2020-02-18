import winsound

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

import py_config as config
import py_logging as log
import py_pandas as conv
import py_path as path


class MyHandler(FTPHandler):
    def on_login(self, username):
        # print("username:%s" % username)
        winsound.Beep(600, 500)
        pass

    def on_connect(self):
        # print("%s:%s connected" % (self.remote_ip, self.remote_port))
        pass

    # 当文件上传完毕时触发
    def on_file_received(self, file):
        logger = log.getLogger()
        logger.debug(file)

        if (path.filenameIsContains(file, 'AAS')):
            conv.convertAASTxt(file)
        if (path.filenameIsContains(file, 'HCS')):
            conv.convertHCSTxt(file)
        if (path.filenameIsContains(file, 'AFS')):
            conv.convertAFSExcel(file)
        winsound.Beep(600, 500)
        pass


def main():
    # 配置管理
    cfg = config.getCfg()

    # 用户管理
    authorizer = DummyAuthorizer()
    usrDist = {
        'username': cfg.get('ftpd', 'username'),
        'password': cfg.get('ftpd', 'password'),
        'homedir': cfg.get('ftpd', 'homedir'),
        'perm': cfg.get('ftpd', 'perm'),
        'msg_login': cfg.get('ftpd', 'msg_login'),
        'msg_quit': cfg.get('ftpd', 'msg_quit')
    }
    authorizer.add_user(**usrDist)

    # 实例化FTPHandler
    handler = MyHandler
    handler.authorizer = authorizer
    handler.banner = "pyftpdlib based ftpd ready."
    address = (cfg.get('ftpd', 'host'), cfg.get('ftpd', 'port'))
    server = FTPServer(address, handler)
    server.max_cons = 256
    server.max_cons_per_ip = 5
    server.serve_forever()


# 运行函数
if __name__ == '__main__':
    main()
