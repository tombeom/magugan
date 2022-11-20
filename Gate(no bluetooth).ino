#include <ESP32Servo.h>

static const int servo1Pin = 19;
Servo servo1;


//CAR IN ULTRA SONIC
int trigPin1 = 5;
int echoPin1 = 18;

//CAR OUT ULTRA SONIC
int trigPin2 = 4;
int echoPin2 = 21;

int duration1;
int distance1;

int duration2;
int distance2;

int flag1 = 0;
int flag2 = 0;

void setup() {
  Serial.begin(115200);
  servo1.attach(19); 
  //servo1.write(100);

  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);

  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);


}


void loop() {
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
    delay (2000);
    servo1.write(100);
    flag1=0, 
    flag2=0;
  }
 Serial.print("Distance: ");
 Serial.println(distance2);
 delay(20);
}
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
