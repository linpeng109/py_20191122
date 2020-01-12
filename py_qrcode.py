import qrcode

data = "1qaz2wsx"

img = qrcode.make(data=data)
img.show()
img.save(r'd:/workspace/baidu.png')
