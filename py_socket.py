# // 获取本机的ip地址

import socket as Socket


def get_host_ip():
    try:
        s = Socket.socket(Socket.AF_INET, Socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()
    finally:
        s.close()
    return ip


if __name__ == '__main__':
    print(get_host_ip()[0])
