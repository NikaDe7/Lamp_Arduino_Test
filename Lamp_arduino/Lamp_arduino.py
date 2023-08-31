import bluetooth
from PyQt5 import QtWidgets, uic
from PyQt5.QtBluetooth import QBluetoothDeviceDiscoveryAgent
from PyQt5.QtCore import QTimer, QEventLoop

app = QtWidgets.QApplication([])
ui = uic.loadUi("des.ui")
ui.setWindowTitle("Test_Lamp")

list_device = []
socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
def startDeviceDiscovery():
    #Create a discovery agent and connect to its signals
    discoveryAgent = QBluetoothDeviceDiscoveryAgent()
    discoveryAgent.deviceDiscovered.connect(deviceDiscover)

    # Start a discovery
    discoveryAgent.start()

    # Create an event loop to manage the execution
    loop = QEventLoop()

    # Set up a timer to exit the event loop after a certain time
    timer = QTimer()
    timer.timeout.connect(loop.quit)
    timer.start(1000)  # 10 seconds

    loop.exec_()

def deviceDiscover(device):
    find_device=device.name()+";"+device.address().toString()
    list_device.append(find_device)

def onOpen():
    address = ui.BluetoothBox.currentText()
    target_address = address.split(';')
    port = 1  # Зазвичай, порт 1 використовується для SPP (Serial Port Profile)

    try:
        socket.connect((target_address[1], port))
        print("Connected to device:", target_address[1])
    except bluetooth.BluetoothError as e:
        print("Connection failed:", str(e))


def onClose():
    socket.close()

def ON():
    data_to_send = b'1'
    socket.send(data_to_send)

def OFF():
    data_to_send = b'0'
    socket.send(data_to_send)

startDeviceDiscovery()
ui.BluetoothBox.addItems(list_device)
ui.OpenButton.clicked.connect(onOpen)
ui.CloseButton.clicked.connect(onClose)

ui.OnButton.clicked.connect(ON)
ui.OffButton.clicked.connect(OFF)

ui.show()
app.exec()

