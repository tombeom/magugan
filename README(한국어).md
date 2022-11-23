
<a name="readme-top"></a>

<p align="right">(<a href="https://github.com/tombeom/magugan/blob/main/README.md#readme-top">ENGLISH</a>)</p>

<br />
<div align="center">
  <a href="https://github.com/tombeom/magugan">
    <img src="images/Logo.png" alt="Logo" width="120" height="120">
  </a>

  <h3 align="center">마구간</h3>

  <p align="center">
    영상처리를 이용한 주차장 정보 시스템
    <br />
    <br />
    <a href="http://tombeom.mynetgear.com:8850/">웹사이트</a>
    ·
    <a href="https://github.com/tombeom/magugan/issues">버그 레포트 하기</a>
    ·
    <a href="https://github.com/tombeom/magugan/blob/main/Team%20Intro.md">팀 원</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>목차</summary>
  <ol>
    <li>
      <a href="#프로젝트">프로젝트</a>
      <ul>
        <li><a href="#사용한-언어">사용한 언어</a></li>
        <li><a href="#보드">보드</a></li>
        <li><a href="#ides">IDEs</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">시작하기</a>
      <ul>
        <li><a href="#필수-구성-요소>-arduino-ide-설치">필수 구성 요소</a></li>
        <li><a href="#arduino-ide에-ESP32-을-설치">Arduino IDE 설치</a></li>
      </ul>
    </li>
    <li><a href="#esp32-선연결">ESP32 선연결</a></li>
    <li><a href="#license">리전즈</a></li>
    <li><a href="#contact">연락</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## 프로젝트

<p align="center">
  <img src="https://github.com/tombeom/magugan/blob/main/images/Project%20picture.JPG" width="750" title="hover text">
</p>

 본 프로젝트는 웹 기반의 사용자 친화 주차장 정보 시스템이다. OpenCV DNN(Deep Neural Network) 모듈을 이용해 객체 감지를 진행하고 주차장 내부의 주차된 차들을 인식한다. 객체 감지로 인식된 정보는 웹페이지에 출력되어 이용자들이 쉽게 주차장 내의 정보를 확인할 수 있다. 웹사이트에는 주차장의 영상 정보와 주차장의 남은 빈자리 수가 출력되고 이 정보는 5초마다 새로고침 된다. 웹사이트는 Python Flask Framework로 구동된다. 객체 감지로 인식된 정보는 블루투스 데이터 송신으로 ESP32 보드에도 전달된다. ESP32 보드에는 해당 정보를 바탕으로 주차장 차단기 역할을 하는 서보모터를 제어한다. 또 두 개의 초음파 센서를 통해 주차장 출입 차량을 인식한다. 본 프로젝트를 통해 기존의 주차장 관리 솔루션 대비 적은 비용으로 시스템을 구축할 수 있고 관리 비용도 절감할 수 있다.

<p align="center">
  <img src="https://github.com/tombeom/magugan/blob/main/images/web%20screenshot.png" width="623.5" height="280" title="hover text">
</p>
<p align="center">
*Screenshot of real time footage*
</p>

### IDEs

<div align="center">

![Thonny](https://img.shields.io/badge/Thonny-Python%20IDE-white?style=for-the-badge&logo=appveyor)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=black)
  
</div>

### 사용한 어언어
<div align="center">
  
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
  ![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)
  ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
  ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
  ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
  
</div>

### 프레임웨크 또는 라이브러리

<div align="center">

![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
[PyBluez library](https://github.com/pybluez/pybluez) 
[ESP32 library](https://github.com/espressif/arduino-esp32)
  
</div>

### 보드

<div align="center">
  
![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white) ![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)
  
</div>

### 딥러닝

<div align="center">

![TensorFlow](https://img.shields.io/badge/TensorFlowLite-%23FF6F00.svg?style=for-the-badge&logo=TensorFlowLite&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
  
</div>
  
<p align="right">(<a href="#readme-top">올라가기</a>)</p>


## 시작하기

### 필수 구성 요소: Arduino IDE 설치

시작하기 전에 컴퓨터에 최신 버전의 Arduino IDE가 설치되어 있는지 확인하

### Arduino IDE에 ESP32 을 설치

Arduino IDE에 ESP32 보드를 설치하기 위해 다음과 같이 합니다:

1. Arduino IDE 에서 File = > Preferences... 로 이동합니다.

<p align="center">
  <img width="300" height="350" src="https://user-images.githubusercontent.com/68363309/202918907-8f328e76-7af5-48e1-9e36-5ed09a0ca782.png">
</p>

2. 아래 주소를 복사해서 입력해줍니다.:

https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

<p align="center">
  <img width="600" height="350" src="https://user-images.githubusercontent.com/68363309/202918993-0eab9b03-7992-4b63-83b0-48bcffed22fc.png">
</p>


"OK" 버튼을 클릭합니다:

3. Tools => Board => Boads Manager 로 이동합니다

<p align="center">
  <img width="600" height="350" src="https://user-images.githubusercontent.com/68363309/202919157-9ce134cc-8425-46a6-a056-64358d8fb910.png">
</p>


4. ESP32 를 입력하고 나온 걸과를 INSTALL 버튼을 클릭하여 설치합니다.

<p align="center">
  <img width="600" height="350" src="https://user-images.githubusercontent.com/68363309/202919236-1e321fba-8152-467a-b69f-7e7d37c869cb.png">
</p>

### ESP32 선연결

<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/68363309/203395504-0a5b0542-634d-4bc4-9cae-ebe41f51c8b5.png">
</p>

ESP32 게이트 어떻게 동작하는지 <a align="center">(<ahref="https://github.com/tombeom/magugan/blob/main/ESP32/Parking%20lot%20gate.md">보기</a>)

<!-- ##################################### Raspberry Pi Bluetooth communication with ESP32 using PYBLUEZ ################################## -->
  
## PYBLUEZ를 사용한 ESP32와의 라즈베리 파이 블루투스 통신
  
1. Pybluez를 설치하고 터미널에 다음 명령을 입력합니다.

```console
$ sudo pip3 install pybluez
$ sudo apt install bluetooth bluez libbluetooth-dev
```

2. 라즈베리 파이톤 코드 다음 명령을 입력합니다.
  
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

<p align="right">(<a href="#readme-top">올라가기</a>)</p>
  
<!-- ##################################### Raspberry Pi OS installation ################################## -->
  
## 탐지 개체 설치 및 준비
    
이 버전에는 라즈베리파이 운영체제 "버스터"를 설치합니다.
  
라즈베리 파이에 라즈베리 PI OS 버스터를 설치하려면 [여기 누르세요](https://maker.pro/raspberry-pi/tutorial/how-to-set-up-raspbian-on-raspberry-pi-4)
  
## 라즈베리 파이 표시
  
1. 터미널의 코드 아래를 실행합니다.
  
```console
$ sudo raspi-config
```
2. 다음 순서에 따라 디스플레이 설정
  
  Display Options - Resolution - DMT Mode 51 
  
3. OpenCV를 설치하기 위한 아래에 코드 입력하십시오
  
```console  
$ pip3 install opencv-python==4.5.1.48
``` 
4. Numpy를 설치하기 위한 아래에 코드 입력하십시오
  
```console  
$ pip3 install numpy==1.20.2
``` 
5. 필요란 라이브러리를 설치하기 위한 아래에 코드 입력하십시오
  
```console  
$ sudo apt-get install libhdf-dev -y
$ sudo apt-get install libhdf-serial-dev -y
$ sudo apt-get install libatlas-base-dev -y
$ sudo apt-get install libjasper-dev -y
$ sudo apt-get install libqtgui4 -y
$ sudo apt-get install libqt4-test -y
``` 
6. TensorFlow를 설치하기 위한 아래에 코드 입력하십시오
  
```console  
$ pip3 install tensorflow==1.14.0
``` 
7. Keras를 설치하기 위한 아래에 코드 입력하십시오
  
```console  
$ pip3 install keras==2.2.5
``` 
* 케라스는 텐서플로 라이브러리의 인터페이스 역할을 한다.
  
8. h5py를 설치하기 위한 아래에 코드 입력하십시오
  
```console  
$ pip3 install h5py==2.10.0
``` 
* h5py 패키지는 HDF5 바이너리 데이터 포맷에 대한 파이토닉 인터페이스이다.
  
<p align="right">(<a href="#readme-top">올라가기</a>)</p>
  
<!-- ##################################### Camera Streaming Server installation ################################## -->
  
## 카메라 스트리밍 서버 설치

카메라 스트리밍 서버의 경우 mjpg-streamer를 사용하고 있습니다.
  
터미널에 아래 코드를 순서대로 배치합니다.

```console  
$ git clone https://github.com/jacksonliam/mjpg-streamer.git
$ cd mjpg-streamer
$ cd mjpg-streamer-experimental
$ sudo apt-get install libjpeg-dev
$ make CMAKE_BUILD_TYPE=Debug
$ sudo make install
``` 
mjpg-streamer 설치 후
  
우리는 "mjpg"라는 이름으로 셸 실행 파일을 만들어야 한다.
  다음 코드는 파일을 생성합니다.

```console  
sudo nano mjpg.sh
```  

<p align="right">(<a href="#readme-top">올라가기</a>)</p>
  
## Usage
  
mjpeg 스트리머 폴더에서:
  
```
export STREAMER_PATH=$HOME/mjpg/mjpg-streamer/mjpg-streamer-experimental
export LD_LIBRARY_PATH=$STREAMER_PATH
$STREAMER_PATH/mjpg_streamer -i "input_uvc.so" -o "output_http.so -w 
$STREAMER_PATH/www"

```
  
#### ** 웹 카메라 대신 라즈베리파이 카메라를 사용하는 경우 아래 줄을 따라 **
  
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

<p align="right">(<a href="#readme-top">올라가기</a>)</p>
