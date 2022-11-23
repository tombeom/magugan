
<a name="readme-top"></a>

<p align="right">(<a href="https://github.com/tombeom/magugan/blob/main/README(%ED%95%9C%EA%B5%AD%EC%96%B4).md">한국어 버전으로 가기</a>)</p>
                                                                
<!-- INTRO -->
                                                                
<br />
<div align="center">
  <a href="https://github.com/tombeom/magugan">
    <img src="images/Logo.png" alt="Logo" width="120" height="120">
  </a>

  <h3 align="center">Magugan</h3>

  <p align="center">
    Parking Lot Vacant Slot Information System Using Image Processing
    <br />
    <br />
    <a href="http://tombeom.mynetgear.com:8850/">Website</a>
    ·
    <a href="https://github.com/tombeom/magugan/issues">Report Bug</a>
    ·
    <a href="https://github.com/tombeom/magugan/blob/main/Team%20Intro.md">Team members</a>
  </p>
</div>

<!-- ############################################################# TABLE OF CONTENTS ################################################################## -->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#ides">IDEs</a></li>
        <li><a href="#languages">Languages</a></li>
        <li><a href="#boards">Boards</a></li>
        <li><a href="#deep-learning">Deep learning</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites: Arduino IDE Installed</a></li>
        <li><a href="#installing-esp32-add-on-in-arduino-ide">Installation of ESP32</a></li>
        <li><a href="#raspberry-pi-bluetooth-communication-with-esp32-using-pybluez">Bluetooth communication</a></li>
        <li><a href="#installation-and-preperation-of-detecting-object">Detecting object</a></li>
        <li><a href="#displaying-raspberrypi">Displaying RaspberryPi</a></li>
        <li><a href="#install-camera-streaming-server">Camera Streaming Server</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ############################################################# ABOUT THE PROJECT ################################################################## -->

## About The Project

<p align="center">
  <img src="https://github.com/tombeom/magugan/blob/main/images/Project%20picture.JPG" width="750" title="hover text">
</p>

Our project is about image processing for a parking lot system which keeps count of the available parking spots. It's done with integrated system made of RaspberryPi algorithm and Arduino board ESP32 . The system recognizes the available spots in the parking lot through a camera input that will then be processed by a deep learning image processing algorithm which output is used to monitor the parking lot situation in real time. A live monitoring is shown on a dedicated website which we made with simple CSS and HTML code. ESP32 and RaspberryPI bluetooth communication performs the function of raising and lowering the breaker (which is build with servo-motor) according to the parking lot situation. The information from the parking lot is shown on the website through web server which built on FLASK. The website displays a real-time footage of the parking lot along with the number of parking slots available. The information is updated every 5 seconds.

<p align="center">
  <img src="https://github.com/tombeom/magugan/blob/main/images/web%20screenshot.png" width="623.5" height="280" title="hover text">
</p>
<p align="center">
*Screenshot of real time footage*
</p>

<!-- ############################################################# BADGES ################################################################## -->

### IDEs

<div align="center">

![Thonny](https://img.shields.io/badge/Thonny-Python%20IDE-white?style=for-the-badge&logo=appveyor)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=black)
  
</div>

### Languages
<div align="center">
  
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
  ![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)
  ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
  ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
  ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
  
</div>

### Frameworks, Platforms and Libraries

<div align="center">

![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
[PyBluez library](https://github.com/pybluez/pybluez) 
[ESP32 library](https://github.com/espressif/arduino-esp32)
  
</div>

### Boards

<div align="center">
  
![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white) ![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)
  
</div>

### Deep learning

<div align="center">

![TensorFlow](https://img.shields.io/badge/TensorFlowLite-%23FF6F00.svg?style=for-the-badge&logo=TensorFlowLite&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
  
</div>
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

<!-- ############################################################# Preperation ################################################################## -->

### Prerequisites

#### Arduino IDE Installed
Before starting this installation procedure, make sure you have the latest version of the Arduino IDE installed in your computer. If you don’t, uninstall it and install it again. Otherwise, it may not work.

<!-- ############################################################# Installation of esp32 ################################################################## -->

### Installing ESP32 Add-on in Arduino IDE

To install the ESP32 board in your Arduino IDE, follow these next instructions:

1. In your Arduino IDE, go to File> Preferences

<p align="center">
  <img width="300" height="350" src="https://user-images.githubusercontent.com/68363309/202918907-8f328e76-7af5-48e1-9e36-5ed09a0ca782.png">
</p>

2. Enter the following into the “Additional Board Manager URLs” field:

https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

<p align="center">
  <img width="600" height="350" src="https://user-images.githubusercontent.com/68363309/202918993-0eab9b03-7992-4b63-83b0-48bcffed22fc.png">
</p>


Then, click the “OK” button:

3. Open the Boards Manager. Go to Tools > Board > Boards Manager…

<p align="center">
  <img width="600" height="350" src="https://user-images.githubusercontent.com/68363309/202919157-9ce134cc-8425-46a6-a056-64358d8fb910.png">
</p>


4. Search for ESP32 and press install button for the “ESP32 by Espressif Systems“:

<p align="center">
  <img width="600" height="350" src="https://user-images.githubusercontent.com/68363309/202919236-1e321fba-8152-467a-b69f-7e7d37c869cb.png">
</p>

<!-- ################################################################### WIRE CONNECTION ################################################################## -->
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### ESP32 Wire Connectioin

<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/68363309/203395504-0a5b0542-634d-4bc4-9cae-ebe41f51c8b5.png">
</p>

<p align="center">(<a href="https://github.com/tombeom/magugan/blob/main/ESP32/Parking%20lot%20gate.md">See more</a>)about how the gate works on ESP32

<!-- ##################################### Raspberry Pi Bluetooth communication with ESP32 using PYBLUEZ ################################## -->
  
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
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ##################################### Raspberry Pi OS installation ################################## -->
  
## Installation and Preperation of Detecting object
    
For this version we have installed RaspberryPi operating system "Buster"
  
To install Raspberry PI OS Buster on Raspberry Pi [Click here](https://maker.pro/raspberry-pi/tutorial/how-to-set-up-raspbian-on-raspberry-pi-4)
  
## Displaying RaspberryPi
  
1. Run below code in the Terminal
  
```console
$ sudo raspi-config
```
2. Set up the Display by following order
  
  Display Options - Resolution - DMT Mode 51 
  
3. Input below code in order to install OpenCV
  
```console  
$ pip3 install opencv-python==4.5.1.48
``` 
4. Input below code in order to install Numpy
  
```console  
$ pip3 install numpy==1.20.2
``` 
5. Input below code in order to install the required libraries
  
```console  
$ sudo apt-get install libhdf-dev -y
$ sudo apt-get install libhdf-serial-dev -y
$ sudo apt-get install libatlas-base-dev -y
$ sudo apt-get install libjasper-dev -y
$ sudo apt-get install libqtgui4 -y
$ sudo apt-get install libqt4-test -y
``` 
6. Input below code in order to install TensorFlow
  
```console  
$ pip3 install tensorflow==1.14.0
``` 
7. Input below code in order to install Keras
  
```console  
$ pip3 install keras==2.2.5
``` 
* Keras acts as an interface for the TensorFlow library. 
  
8. Input below code in order to install h5py
  
```console  
$ pip3 install h5py==2.10.0
``` 
* The h5py package is a Pythonic interface to the HDF5 binary data format. 
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>
  
<!-- ##################################### Camera Streaming Server installation ################################## -->
  
## Install Camera Streaming Server

For Camera streaming server we are using mjpg-streamer
  
Put below codes in the Terminal in order

```console  
$ git clone https://github.com/jacksonliam/mjpg-streamer.git
$ cd mjpg-streamer
$ cd mjpg-streamer-experimental
$ sudo apt-get install libjpeg-dev
$ make CMAKE_BUILD_TYPE=Debug
$ sudo make install
``` 
After the installation of mjpg-streamer
  
We have to make shell executable file under name of "mjpg"
   following code will create the file

```console  
sudo nano mjpg.sh
```  

<p align="right">(<a href="#readme-top">back to top</a>)</p>
  
## Usage
  
From the mjpeg streamer folder:
  
```
export STREAMER_PATH=$HOME/mjpg/mjpg-streamer/mjpg-streamer-experimental
export LD_LIBRARY_PATH=$STREAMER_PATH
$STREAMER_PATH/mjpg_streamer -i "input_uvc.so" -o "output_http.so -w 
$STREAMER_PATH/www"

```
  
#### ** in case if you use raspberrypi camera instead of webcamera follow below lines **
  
```
export STREAMER_PATH=$HOME/mjpg/mjpg-streamer/mjpg-streamer-experimental
export LD_LIBRARY_PATH=$STREAMER_PATH
$ STREAMER_PATH/mjpg_streamer -i "input_raspicam.so" -o "output_http.so -w 
$ STREAMER_PATH/www"

```  
  
  <!-- CONTACT -->
## Contact

tombeom - tombeom@naver.com </br>
Zolboo - zolboo.oz@gmail.com </p>
Project Link: [https://github.com/tombeom/magugan)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
 

