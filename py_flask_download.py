# 启动webfuw
# import py_watchdog as watchdog
import subprocess

from flask import send_from_directory, Flask

import py_socket as s

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


def callable(result):
    print(result)
    return result


@app.route('/download')
def download():
    return send_from_directory('d:/', 'test.docx')


if __name__ == '__main__':
    p = subprocess.Popen(['./py_watchdog.exe'], stdout=subprocess.PIPE)
    # watchdog.startObserver()
    print('localhost ip is %s' % s.get_host_ip()[0])
    app.run(host='0.0.0.0', port=8822)
    # _result = p.stdout.readlines()
    # for line in _result:
    #     print(line)
