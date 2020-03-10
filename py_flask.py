from io import BytesIO

from flask import Flask, send_file
from pandas.tests.io.excel.test_xlsxwriter import xlsxwriter

import py_kafka_producer as producer
import py_uipath as uipath

app = Flask(__name__, static_url_path='')
app.permanent_session_lifetime = 2000


@app.route('/')
def helloWorld():
    return 'Hello World'


def callback(result):
    print(result)
    return result


@app.route("/download", methods=["GET"])
def download():
    out = BytesIO()
    workbook = xlsxwriter.Workbook(out)
    table = workbook.add_worksheet()
    table.write(0, 0, "此处显示唯一ID")
    table.write(0, 1, "此处显示二维码图片")
    workbook.close()
    out.seek(0)
    return send_file(out, as_attachment=True, attachment_filename="dream.xlsx")


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
    # producer.send(result, callback)
    return result


@app.route('/uipath/lims')
def limscommand():
    _lines = uipath.commander(cmd=uipath.lims)
    result = ''
    for line in _lines:
        result = result + str(line)
    # print(result)
    producer.send(result, callback)
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
