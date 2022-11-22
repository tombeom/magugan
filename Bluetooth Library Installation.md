## Raspberry Pi Bluetooth communication with ESP32 using PYBLUEZ 
     
1. Install pybluez for Python3, enter the command in Terminal:

```console
$ sudo pip3 install pybluez
$ sudo apt install bluetooth bluez libbluetooth-dev
```
2. Put below python code in Raspberry Pi Thonny.

```python
from bluetooth import *
def sendData():
    print("\nType something\n")
    while True:
        data = input()
        if len(data) == 0: break
        sock.send(data)
        sock.send("\n")           
#MAC address of ESP32
addr = "24:0A:C4:E8:0F:9A"
service_matches = find_service( address = addr )

buf_size = 1024;

if len(service_matches) == 0:
    print("couldn't find the SampleServer service =(")
    sys.exit(0)

for s in range(len(service_matches)):
    print("\nservice_matches: [" + str(s) + "]:")
    print(service_matches[s])
    
first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]
port=1
print("connecting to \"%s\" on %s, port %s" % (name, host, port))

# Create the client socket
sock=BluetoothSocket(RFCOMM)
sock.connect((host, port))

print("connected")
sendData()
sock.close()
```
