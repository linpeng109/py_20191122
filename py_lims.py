from PySide2.QtWidgets import QApplication, QWidget, QLabel
import sys
from PySide2.QtGui import QIcon, QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PSide2 Simple Window")
        self.setGeometry(300, 300, 600, 300)
        self.setMinimumHeight(100)
        self.setIcon()
        self.setIconModes()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def setIconModes(self):
        icon1 = QIcon("icon.png")
        label1 = QLabel('sample', self)
        pixmap1 = icon1.pixmap(100, 100, QIcon.Active, QIcon.On)
        label1.setPixmap(pixmap1)


myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)
