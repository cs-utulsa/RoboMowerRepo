#define motor1PWM 9
#define motor1IN2 2
#define motor1IN1 3

#define motor2PWM 10
#define motor2IN2 4
#define motor2IN1 5

#define motor3PWM 11
#define motor3IN4 6
#define motor3IN3 7

void setup() {
  // front right wheel
  pinMode(motor1PWM, OUTPUT);
  pinMode(motor1IN1, OUTPUT);
  pinMode(motor1IN2, OUTPUT);

  // front left wheel
  pinMode(motor2PWM, OUTPUT);
  pinMode(motor2IN1, OUTPUT);
  pinMode(motor2IN2, OUTPUT);

  // rear wheel
  pinMode(motor3PWM, OUTPUT);
  pinMode(motor3IN4, OUTPUT);
  pinMode(motor3IN3, OUTPUT);
}

void loop() {

  // spin all wheels (testing)
//  analogWrite(motor1PWM, 255); //establish speeds for the motors (range: 0-255)
//  analogWrite(motor2PWM, 255);
//  analogWrite(motor3PWM, 255);
//
//  digitalWrite(motor1IN1, HIGH);
//  digitalWrite(motor1IN2, LOW);
//  digitalWrite(motor2IN1, HIGH);
//  digitalWrite(motor2IN2, LOW);
//  digitalWrite(motor3IN4, HIGH);
//  digitalWrite(motor3IN3, LOW);
//
//  delay(1000);
//
//  analogWrite(motor1PWM, 255); //establish speeds for the motors (range: 0-255)
//  analogWrite(motor2PWM, 255);
//  analogWrite(motor3PWM, 255);
//
//  digitalWrite(motor1IN1, LOW);
//  digitalWrite(motor1IN2, HIGH);
//  digitalWrite(motor2IN1, LOW);
//  digitalWrite(motor2IN2, HIGH);
//  digitalWrite(motor3IN4, LOW);
//  digitalWrite(motor3IN3, HIGH);
//
//  delay(1000);
  
  //forward
//  analogWrite(motor1PWM, 100); //establish speeds for the motors (range: 0-255)
//  analogWrite(motor2PWM, 100);
//  analogWrite(motor3PWM, 100);
//
//  digitalWrite(motor1IN1, HIGH); // clockwise
//  digitalWrite(motor1IN2, LOW);
//  digitalWrite(motor2IN1, LOW); // counter clockwise
//  digitalWrite(motor2IN2, HIGH);
//  digitalWrite(motor3IN4, LOW); // off
//  digitalWrite(motor3IN3, LOW);
//
//  delay(500);
//
//  // stop for 2 seconds
//  analogWrite(motor1PWM, 0);
//  analogWrite(motor2PWM, 0);
//  analogWrite(motor3PWM, 0);
//
//  digitalWrite(motor1IN1, LOW);
//  digitalWrite(motor1IN2, LOW);
//  digitalWrite(motor2IN1, LOW);
//  digitalWrite(motor2IN2, LOW);
//  digitalWrite(motor3IN4, LOW);
//  digitalWrite(motor3IN3, LOW);
//
//  delay(2000);
//
//  // backwards
//  analogWrite(motor1PWM, 100);
//  analogWrite(motor2PWM, 100);
//  analogWrite(motor3PWM, 100);
//
//  digitalWrite(motor1IN1, LOW); // counter clockwise
//  digitalWrite(motor1IN2, HIGH);
//  digitalWrite(motor2IN1, HIGH); // clockwise
//  digitalWrite(motor2IN2, LOW);
//  digitalWrite(motor3IN4, LOW);
//  digitalWrite(motor3IN3, LOW);
//
//  delay(500);
//
//  // stop for 2 seconds
//  analogWrite(motor1PWM, 0);
//  analogWrite(motor2PWM, 0);
//  analogWrite(motor3PWM, 0);
//
//  digitalWrite(motor1IN1, LOW);
//  digitalWrite(motor1IN2, LOW);
//  digitalWrite(motor2IN1, LOW);
//  digitalWrite(motor2IN2, LOW);
//  digitalWrite(motor3IN4, LOW);
//  digitalWrite(motor3IN3, LOW);
//
//  delay(2000);

  // right
//  analogWrite(motor1PWM, 150);
//  analogWrite(motor2PWM, 150);
//  analogWrite(motor3PWM, 250);
//
//  digitalWrite(motor1IN1, LOW); // counter clockwise
//  digitalWrite(motor1IN2, HIGH);
//  digitalWrite(motor2IN1, LOW); // clockwise
//  digitalWrite(motor2IN2, HIGH);
//  digitalWrite(motor3IN4, HIGH); // clockwise
//  digitalWrite(motor3IN3, LOW);
//
//  delay(1500);

  // stop for 2 seconds
//  analogWrite(motor1PWM, 0);
//  analogWrite(motor2PWM, 0);
//  analogWrite(motor3PWM, 0);
//
//  digitalWrite(motor1IN1, LOW);
//  digitalWrite(motor1IN2, LOW);
//  digitalWrite(motor2IN1, LOW);
//  digitalWrite(motor2IN2, LOW);
//  digitalWrite(motor3IN4, LOW);
//  digitalWrite(motor3IN3, LOW);
//
//  delay(2000);
//
//  // left
  analogWrite(motor1PWM, 100);
  analogWrite(motor2PWM, 100);
  analogWrite(motor3PWM, 250);

  digitalWrite(motor1IN1, HIGH); // clockwise
  digitalWrite(motor1IN2, LOW);
  digitalWrite(motor2IN1, HIGH); // clockwise
  digitalWrite(motor2IN2, LOW);
  digitalWrite(motor3IN4, LOW); // counter clockwise
  digitalWrite(motor3IN3, HIGH);

  delay(1500);

  // stop for 5 seconds
  analogWrite(motor1PWM, 0);
  analogWrite(motor2PWM, 0);
  analogWrite(motor3PWM, 0);

  digitalWrite(motor1IN1, LOW);
  digitalWrite(motor1IN2, LOW); 
  digitalWrite(motor2IN1, LOW);
  digitalWrite(motor2IN2, LOW);
  digitalWrite(motor3IN4, LOW);
  digitalWrite(motor3IN3, LOW);

  delay(5000);
}
