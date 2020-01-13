import pyzbar.pyzbar as pyzbar
import PIL.Image as Image

filename = 'd:/workspace/baidu.png'
img = Image.open(filename)
zbardata = pyzbar.decode(img)
print(zbardata)
