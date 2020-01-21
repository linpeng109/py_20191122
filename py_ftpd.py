from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import winsound
import py_excel


class MyHandler(FTPHandler):
    def __init__(self):
        return "null"

    def on_login(self, username):
        print("username:%s" % username)
        # winsound.Beep(600, 500)
        pass

    def on_connect(self):
        print("%s:%s connected" % (self.remote_ip, self.remote_port))
        # winsound.Beep(600, 1000)
        pass
    # 当文件上传完毕时触发
    def on_file_received(self, file):

        py_excel.main(file)
        winsound.Beep(600, 1000)
        pass


def main():
    # 用户管理
    authorizer = DummyAuthorizer()
    authorizer.add_user(username='user', password='12345', homedir='d:/ftpdir', perm='elradfmwMT',
                        msg_login='hello world', msg_quit='Goodbye')
    # authorizer.add_anonymous('d:/ftpdir')

    # 实例化FTPHandler
    handler = MyHandler
    handler.authorizer = authorizer
    handler.banner = "pyftpdlib based ftpd ready."
    address = ('localhost', 8821)
    server = FTPServer(address, handler)
    server.max_cons = 256
    server.max_cons_per_ip = 5
    server.serve_forever()


# 运行函数
if __name__ == '__main__':
    main()
