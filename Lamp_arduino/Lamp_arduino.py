from PyQt5 import QtWidgets, uic
from PyQt5.QtBluetooth import QBluetoothDeviceInfo, QBluetoothDeviceDiscoveryAgent, QBluetoothLocalDevice

from PyQt5.QtCore import QIODevice, pyqtSlot, QCoreApplication

app = QtWidgets.QApplication([])
ui = uic.loadUi("des.ui")
ui.setWindowTitle("Test_Lamp")


def startDeviceDiscovery():
    app = QCoreApplication([])

    # Create a discovery agent and connect to its signals
    discoveryAgent = QBluetoothDeviceDiscoveryAgent()
    discoveryAgent.deviceDiscovered.connect(deviceDiscovered)

    # Start a discovery
    discoveryAgent.start()

    app.exec_()

@pyqtSlot(QBluetoothDeviceInfo)
def deviceDiscovered(device):
    print(f"Found device: {device.name()} ({device.address().toString()})")

startDeviceDiscovery()

ui.show()
app.exec()