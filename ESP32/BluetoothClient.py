from bluetooth import*
import time
# 여기 rawData에 주차장 full인지 아닌지 데이터를 입력
rawData = 0
def send_data():
     while True:
          data = rawData
          if len(data) == 0: break
          sock.send(data)
          sock.send("\n")


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

send_data()
sock.close()
print("\n--- bye ---\n")
