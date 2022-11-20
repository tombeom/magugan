from bluetooth import*
import time
def closeGate():
     print("\nClosing gate\n")
     #while True:
     data = 0;
     sock.send( (data))
     sock.send("\n")
     time.sleep(1)
def openGate():
     print("\nOpening gate\n")
     #while True:
     data = 90;
     sock.send(str(data))
     sock.send("\n")
     time.sleep(1)

def input_and_send():
     print("\nType something\n")
     while True:
         data = input()
         if len(data) == 0: break
         sock.send(data)
         sock.send("\n")

def rx_and_echo():
     sock.send("\nsend anything\n")
     while True:
         data = sock.recv(buf_size)
         if data:
             print(data.decode('utf-8'))
             sock.send(data)

 #MAC Address of esp32
addr = "94:B5:55:F8:2F:02"
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
#service_matches = find_service(uuid = uuid, address = addr)
service_matches = find_service( address = addr)


buf_size = 1024;

if len(service_matches) == 0:
    print("could not find the sampleserver service =(")
    sys.exit(0)
for s in range(len(service_matches)):
     print("\nservice_matches: [" + str(s) + "]:")
     print(service_matches[s])

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

port=1

print("connecting to \"%s\" on %s, port %s" % (name,host,port))

# Create the client socket
sock = BluetoothSocket(RFCOMM)
sock.connect((host, port))

print("connected")

input_and_send()
#rx_and_echo()
sock.close()
print("\n--- bye ---\n")
