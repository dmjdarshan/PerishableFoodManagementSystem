import sys
import pymongo

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QMenuBar,
)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Goods Management System")
        
    def initUI(self):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    App = App()
    App.show()
    sys.exit(app.exec_())