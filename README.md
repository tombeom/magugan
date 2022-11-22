
<a name="readme-top"></a>

<p align="https://github.com/tombeom/magugan/blob/main/README(%ED%95%9C%EA%B5%AD%EC%96%B4).md">(<a href="link">한국어 버전으로 가기</a>)</p>

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
    <a href="link">Website</a>
    ·
    <a href="https://github.com/tombeom/magugan/issues">Report Bug</a>
    ·
    <a href="https://github.com/tombeom/magugan/blob/main/Team%20Intro.md">Team members</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#languages">Languages</a></li>
        <li><a href="#boards">Boards</a></li>
        <li><a href="#ides">IDEs</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites>-arduino-ide-installed">Prerequisites: Arduino IDE Installed</a></li>
        <li><a href="#installing-esp32-add-on-in-arduino-ide">Installation of ESP32</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<p align="center">
  <img src="https://github.com/tombeom/magugan/blob/main/images/Project%20picture.JPG" width="750" title="hover text">
</p>

Our project is about image processing for a parking lot system which keeps count of the available parking spots. It's done with integrated system made of RaspberryPi algorithm and Arduino. The system recognizes the remaining spots in the parking lot through a camera input that will then be processed by a deep learning image processing algorithm which output is used to monitor the parking lot situation in real time. A live monitoring is shown on a dedicated website which we are in a process of making it. Arduino and Bluetooth communication perform the function of raising and lowering the breaker according to the parking lot situation. The information from the parking lot will be shown on the website through web server.

### Languages
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)


### Boards

![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white) ![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)

### IDEs

![Thonny](https://img.shields.io/badge/Thonny-Python%20IDE-white?style=for-the-badge&logo=appveyor)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=black)

### Libraries


[PyBluez](https://github.com/pybluez/pybluez) 

[ESP32](https://github.com/espressif/arduino-esp32)
  
  
  
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

1. Install Raspian on RaspberryPi
2. Installation of ESP32

### Prerequisites> Arduino IDE Installed

Before starting this installation procedure, make sure you have the latest version of the Arduino IDE installed in your computer. If you don’t, uninstall it and install it again. Otherwise, it may not work.

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

### ESP32 Wire Connectioin

<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/68363309/203395504-0a5b0542-634d-4bc4-9cae-ebe41f51c8b5.png">
</p>

<p align="center">(<a href="https://github.com/tombeom/magugan/blob/main/ESP32/Parking%20lot%20gate.md">See more</a>)about how the gate works on ESP32

  <!-- CONTACT -->
## Contact

Tombeom - tombeom@naver.com </br>
Zolboo - zolboo.oz@gmail.com </p>
Project Link: [https://github.com/tombeom/magugan)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
 

