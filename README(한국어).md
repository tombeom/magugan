
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

영상처리를 이용한 주차장 정보 시스템은 라즈베리파이와 아두이노의 통합 시스템으로 구성하여 운영된다. 라즈베리파이의 카메라를 통해 영상 정보를 입력받고 딥러닝 이미지 처리를 통해 주차된 자동차를 인식한다. HTML과 CSS를 이용해 웹페이지를 구성하고 웹서버를 통해 주차장의 실시간 상태를 이용자에게 표시한다. 아두이노는 라즈베리파이로부터 주차장의 상태를 블루투스로 전달받고 서보모터를 사용해 주차 차단기를 내리고 올리는 등의 기능을 수행한다.

### 사용한 언어
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)


### 보드

![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white) ![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)

### IDEs

![Thonny](https://img.shields.io/badge/Thonny-Python%20IDE-white?style=for-the-badge&logo=appveyor)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=black)

### Libraries


[PyBluez](https://github.com/pybluez/pybluez) 

[ESP32](https://github.com/espressif/arduino-esp32)
  
  
  
  
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

<p align="center">(<a href="https://github.com/tombeom/magugan/blob/main/ESP32/Parking%20lot%20gate.md">See more</a>)about how the gate works on ESP32

  <!-- CONTACT -->
## 

Tombeom - tombeom@naver.com </br>
Zolboo - zolboo.oz@gmail.com </p>
힛 링크: (https://github.com/tombeom/magugan)

<p align="right">(<a href="#readme-top">올라가기</a>)</p>
 

