#include <ESP32Servo.h>
#include "BluetoothSerial.h"
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

static const int servo1Pin = 19; //printed G19 on the board

Servo servo1;  //Declaring servo motor
//CAR IN ULTRA SONIC 차 들어왔을 때
int trigPin1 = 5;
int echoPin1 = 18;

int CHECK;
int CHECK1;
//CAR OUT ULTRA SONIC 차 나갔을 때
int trigPin2 = 4;
int echoPin2 = 21;

//서버 머터를 계산하기 위한 코드
int duration1;
int distance1;
int duration2;
int distance2;

//차를 양벙향으로 가오도록 하기 위한 카온터
int flag1 = 0;
int flag2 = 0;

//블루투스 declaring
BluetoothSerial SerialBT;
String inData;

// Received value will be stored as CHAR in this variable
char receivedChar;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32 bluetooth"); //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");
  servo1.attach(servo1Pin);
  
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
}

void loop() {

  
  //Servo with ESP32 Bluetooth
  if (Serial.available()) {
    SerialBT.write(Serial.read());
  }
  //Recieve data from RaspberryPi
  while (SerialBT.available() ) {             
    receivedChar =(char)SerialBT.read();
    inData += receivedChar;    
        if (receivedChar == '\n')
        {    
        // write on pi   
        SerialBT.print("Received:");
        SerialBT.println(inData);
        //print on Serial Monitor
        Serial.print("Received:");
        Serial.println(inData);
        //convert it to integer  
        CHECK = inData.toInt() ;
        // Clear recieved buffer                    
        inData = "";           
        }
  }
  delay(20);
  Serial.print("check ");
  Serial.println(CHECK);
  delay(500);
  CHECK1 = CHECK;
if(CHECK1 != 6){
  ultra_sonic();
  if(distance1 < 10 && flag1==0){
      flag1=1;
      if(flag2==0){
        servo1.write(0);
      }
  }
  if(distance2 < 10 && flag2==0){
    flag2=1;
    if(flag1==0){
    servo1.write(0); 
    }
  }
  if(flag1==1 && flag2==1){
    delay (1000);
    servo1.write(100);
    flag1=0, 
    flag2=0;
  }
 //Serial.println("Distance1: " + distance1 + "Distance2" + distance2);
 delay(20);
}


}//void loop ends here

//ultra sonic method for calculating distance for the sensor
void ultra_sonic(){
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);
  duration1 = pulseIn(echoPin1, HIGH);
  distance1 = duration1*0.034/2;
  //ultra2
  digitalWrite(trigPin2, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);
  duration2 = pulseIn(echoPin2, HIGH);
  distance2 = duration2*0.034/2;
}
