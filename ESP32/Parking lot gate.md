# Parking lot gate

## Board  : ESP32
## Sensor : Ultrasonic Sensor
## Motor  : Servo motor

![image](https://user-images.githubusercontent.com/68363309/202601823-7c17cbe1-cb20-4634-b2d9-2f73f00d0054.png)

### How it works step by step : 

#### ▦ 1 When object [Car] is in-front of one of the ultrasonic sensors, it detects it and triggers Servo motor and opens the gate

![image](https://user-images.githubusercontent.com/68363309/202603874-5b5dfd95-d282-4b13-8639-6ef23eed9dc9.png)


#### ▦ 2 After object [Car] passed through the gate, it will trigger the second ultrasonic sensor -> triggers the servo motor and closes the gate

![image](https://user-images.githubusercontent.com/68363309/202604809-bc218953-53c7-4c88-b000-72be3a29d2f1.png)




