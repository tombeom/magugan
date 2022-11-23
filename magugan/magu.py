import threading
import time
import cv2
from bluetooth import *

# Set pretrained TensorFlow Object Detection weights model and config file path
weightsModel = "/home/magu/magugan/models/frozen_inference_graph_V2.pb"
configFile = "/home/magu/magugan/models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt"
# Read TensorFlow DNN(Deep Neural Network)
cv2DNN = cv2.dnn.readNetFromTensorflow(weightsModel, configFile)

# Set video stream URL
# When receive camera input directly (cv2.VideoCapture(int CameraIndex(-1 ~ )))
cameraStreamUrl = "http://192.168.1.31:8080/?action=stream"
camera = cv2.VideoCapture(cameraStreamUrl)

def objDetect():
    global image
    global imgRead
    global carCnt
    global sendData
    while True:
        # Initialize value
        imgRead = 0
        carCnt = 0
        # If read image successful, Keep going
        if imgRead == 1:
            # Get image height, width, channel (When color image)
            imgHeight, imgWidth, imgChannel = image.shape
            # Make input image to blob object, Function cv2.dnn.blobFromImage() returns 4-dimensional blob object with N,C,H,W demensions
            # Set image size to (500, 500)
            blob = cv2.dnn.blobFromImage(image, size=(500, 500))
            # Input blob object to DNN
            cv2DNN.setInput(blob)
            # Run forward pass
            outputBlob = cv2DNN.forward()
            for detectedInfo in outputBlob[0, 0, :, :]:
                # Detect only car
                if isCar(detectedInfo[1]) == True:
                    # Detect when accuracy is greater than {}
                    if detectedInfo[2] > .80:
                        # start point from top-left corner
                        startPoint = (int(detectedInfo[3] * imgWidth), int(detectedInfo[4] * imgHeight))
                        # end point from bottom-right corner
                        endPoint = (int(detectedInfo[5] * imgWidth), int(detectedInfo[6] * imgHeight))
                        # Set box color
                        color = (0, 255, 0)
                        # Make rectangle on detected object
                        cv2.rectangle(image, startPoint, endPoint, color, thickness=3)
                        # Add carCnt value
                        carCnt += 1
            # Display image on screen
            cv2.imshow('Parking Lot Car Detection', image)
            # Send data to other
            sendData = carCnt
            saveData()

def readImg():
    # Read image every 1 sec
    global image
    global imgRead
    global carCnt
    
    try: 
        while True:
            # Wait {} second(s) for key input (In this case, Just wait 1 sec)
            cv2.waitKey(1)

            imgRead = 0
            # Function .read() returns boolean and array value
            imgBool, image = camera.read()
            imgRead = 1
    except:
        pass

def btCom():
    global sendData
    sendData = 0
    #MAC Address of esp32
    addr = "94:B5:55:F8:2F:02"
    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    #service_matches = find_service(uuid = uuid, address = addr)
    service_matches = find_service(address = addr)


    buf_size = 1024

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
    
    while True:
        sock.send(str(sendData))
        sock.send("\n")
        print("Sent Data(%d) to esp32" %sendData)
        time.sleep(2)

    sock.close()
    print("\n--- bye ---\n")


def isCar(detectionValue):
    # 3.0 is Car
    # If detect car, Return true else nothing
    if detectionValue == 3.0:
        return True
    else:
        return False

def saveData():
    # Parking lot maximum count
    MAXCARCNT = 6
    # How many car detected value
    global carCnt

    # If detect more than maximum count (When error occurred), Adjust carCnt value to maximum count
    if carCnt > MAXCARCNT:
        carCnt = 6
    leftCarCnt = MAXCARCNT - carCnt
    
    # Print carCnt value to console
    print("%d car(s) Detected" %carCnt)
    
    # Write carCnt value to txt file
    with open("/home/magu/magugan/carCnt.txt", "w") as file:
        file.write(str(leftCarCnt))
    # After write, Print message to console
    print("Write Complete")
    # Sleep {} seconds(s)
    time.sleep(2)


if __name__ == '__main__':
    # Make threads and start
    task1 = threading.Thread(target = objDetect)
    task2 = threading.Thread(target = readImg)
    task3 = threading.Thread(target = btCom)
    task1.start()
    task2.start()
    task3.start()