from PyQt5 import QtWidgets, uic

from PyQt5.QtCore import QIODevice

app = QtWidgets.QApplication([])
ui = uic.loadUi("des.ui")
ui.setWindowTitle("Test_Lamp")

ui.show()
app.exec()