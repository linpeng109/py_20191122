import qrcode


def getQRCode(data):
    img = qrcode.make(data=data)
    return img


if __name__ == '__main__':
    data = "1qaz2wsx"
    img = getQRCode(data=data)
    img.show()
    # img.save(r'd:/workspace/baidu.png')
