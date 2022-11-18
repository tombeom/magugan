{
  "version": 1,
  "author": "ODONKHUU ZOLBOO",
  "parts": [
    { "type": "esp32-devkit-v1", "id": "esp", "top": 0, "left": 0, "attrs": {} },
    {
      "type": "hc-sr04",
      "id": "ultrasonic1",
      "top": -122.12,
      "left": 196.53,
      "attrs": { "distance": "113" }
    },
    { "type": "servo", "id": "servo1", "top": -135.67, "left": 391.28, "attrs": {} },
    {
      "type": "hc-sr04",
      "id": "ultrasonic2",
      "top": -117.73,
      "left": 605.28,
      "attrs": { "distance": "168" }
    }
  ],
  "connections": [
    [ "esp:TX0", "$serialMonitor:RX", "", [] ],
    [ "esp:RX0", "$serialMonitor:TX", "", [] ],
    [ "esp:3V3", "ultrasonic1:VCC", "green", [ "v-3.24", "h163.03" ] ],
    [ "ultrasonic1:GND", "esp:GND.1", "black", [ "v176.13", "h-9.65" ] ],
    [ "servo1:GND", "esp:GND.1", "black", [ "h-25.75", "v235.3" ] ],
    [ "servo1:PWM", "esp:D19", "green", [ "h-4.38", "v199.44" ] ],
    [ "servo1:V+", "esp:3V3", "green", [ "h-17.42", "v236.75" ] ],
    [ "ultrasonic2:VCC", "esp:3V3", "red", [ "v0" ] ],
    [ "ultrasonic2:GND", "esp:GND.1", "black", [ "v0" ] ],
    [ "ultrasonic1:TRIG", "esp:D4", "green", [ "v0" ] ],
    [ "ultrasonic1:ECHO", "esp:D21", "green", [ "v0" ] ],
    [ "ultrasonic2:ECHO", "esp:D18", "green", [ "v0" ] ],
    [ "ultrasonic2:TRIG", "esp:D5", "green", [ "v0" ] ]
  ]
}
