#include <Servo.h>

int sensor_right = 7;
int sensor_left = 5;

Servo servoRight;
Servo servoLeft;

void forward(){
  servoRight.writeMicroseconds(1300);
  servoLeft.writeMicroseconds(1700);
}
void backward(){
  servoRight.writeMicroseconds(1700);
  servoLeft.writeMicroseconds(1300);
}
void left(){
  servoRight.writeMicroseconds(1300);
  servoLeft.writeMicroseconds(1300);
}
void right(){
  servoRight.writeMicroseconds(1700);
  servoLeft.writeMicroseconds(1700);
}
void stopping(){
  servoRight.writeMicroseconds(1500);
  servoLeft.writeMicroseconds(1500);
}

void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(9600);
  
  servoLeft.attach(11);
  servoRight.attach(12);
  stopping();
  pinMode(sensor_right, INPUT_PULLUP);
  pinMode(sensor_left, INPUT_PULLUP);
  digitalWrite(sensor_right,HIGH);
  digitalWrite(sensor_left, HIGH);
}
void loop(){
//  digitalRead(sensor_right);
//  digitalRead(sensor_left);
  
  if (digitalRead(sensor_left)== LOW && digitalRead(sensor_right)== LOW){
    Serial.print("I am HIGHHHHH");
    backward();
    delay(200);
    left();
    delay(500);
    forward();
    delay(1500);
  }
  else if (digitalRead(sensor_right) == LOW && digitalRead(sensor_left)== HIGH){
    Serial.print("sensor right is HIGHH");
    backward();
    delay(200);
    left();
    delay(500);
    forward();
    delay(500);
  }
  else if (digitalRead(sensor_left) == LOW && digitalRead(sensor_right)== HIGH){
    Serial.print("sensor left is HIGHHH");
    backward();
    delay(200);
    right();
    delay(500);
    forward();
    delay(500);
  }
  else if (digitalRead(sensor_left) == HIGH && digitalRead(sensor_right)== HIGH){
    Serial.print("both are low");
    forward();
  }
 }


