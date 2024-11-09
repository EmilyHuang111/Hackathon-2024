#include <Arduino.h>
#include <MeMCore.h>

MeUltrasonicSensor ultraSonic(PORT_3);
MeDCMotor motor_left(M1);
MeDCMotor motor_right(M2);

void setup() {
  Serial.begin(9600); // Adjust the baud rate if needed
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    switch (command) {
      case 'F': // Move forward
        motor_left.run(-255); 
        motor_right.run(255);
        break;
      case 'B': // Move backward
        motor_left.run(255);
        motor_right.run(-255);
        break;
      case 'L': // Turn left
        motor_left.run(255);
        motor_right.run(255);
        break;
      case 'R': // Turn right
        motor_left.run(-255);
        motor_right.run(-255);
        break;
      case 'S': // Stop
        motor_left.run(0);
        motor_right.run(0);
        break;
      case 'U': // Ultrasonic
        float distance = ultraSonic.distanceCm();
        Serial.println(distance);

    }
  }
}
