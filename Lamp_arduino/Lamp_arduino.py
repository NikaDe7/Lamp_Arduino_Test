from PyQt5 import QtWidgets, uic
from PyQt5.QtBluetooth import QBluetoothDeviceInfo, QBluetoothDeviceDiscoveryAgent, QBluetoothLocalDevice
from PyQt5.QtCore import QIODevice, pyqtSlot, QCoreApplication, QTimer, QEventLoop

app = QtWidgets.QApplication([])
ui = uic.loadUi("des.ui")
ui.setWindowTitle("Test_Lamp")

list_device = []

def startDeviceDiscovery():
    # Create a discovery agent and connect to its signals
    discoveryAgent = QBluetoothDeviceDiscoveryAgent()
    discoveryAgent.deviceDiscovered.connect(deviceDiscover)

    # Start a discovery
    discoveryAgent.start()

    # Create an event loop to manage the execution
    loop = QEventLoop()

    # Set up a timer to exit the event loop after a certain time
    timer = QTimer()
    timer.timeout.connect(loop.quit)
    timer.start(3000)  # 10 seconds

    loop.exec_()
def deviceDiscover(device):
    print(f"Found device: {device.name()} ({device.address().toString()})")
    find_device=device.name()+" "+device.address().toString()
    list_device.append(find_device)

startDeviceDiscovery()
print(list_device)
ui.BluetoothBox.addItems(list_device)

ui.show()
app.exec()

