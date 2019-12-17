from flask import Flask

import py_kafka_producer as producer
import py_uipath as uipath

app = Flask(__name__)


@app.route('/')
def helloWorld():
    return 'Hello World'


def callback(result):
    print(result)
    return result


@app.route('/kafka/send/<topic>/<msg>', methods=['post'])
def send(topic, msg):
    producer.send(msg, callback)
    return str(topic) + str(msg)


@app.route('/uipath/editplus')
def uipathcommand():
    _lines = uipath.commander(cmd=uipath.editplus)
    result = ''
    for line in _lines:
        result = result + str(line)
    # print(result)
    producer.send(result, callback)
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0')
