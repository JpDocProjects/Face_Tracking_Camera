#include <Servo.h>

Servo servo_y;
Servo servo_x;

float x_pos = 90;
float y_pos = 70;

float value = 4.0;

float K = 0.048;

float last_error_x;
float last_error_y;

void setup() {
  Serial.begin(9600);

  servo_y.attach(6);
  servo_x.attach(5);

  servo_x.write(x_pos);
  servo_y.write(y_pos);
}

void loop() {
  if (Serial.available()){
    String data = Serial.readStringUntil('\n');
    int commaIndex = data.indexOf(',');

    String part1 = data.substring(0, commaIndex);
    String part2 = data.substring(commaIndex + 1);

    float error_x = part1.toFloat();
    float error_y = part2.toFloat();

    if (abs(error_x) > value || abs(error_y) > value){
      x_pos -= (K * error_x);
      x_pos = constrain(x_pos, 0, 180);
      servo_x.write(x_pos);

      y_pos += (K * error_y);
      y_pos = constrain(y_pos, 0, 120);
      servo_y.write(y_pos);
    }
  }
}