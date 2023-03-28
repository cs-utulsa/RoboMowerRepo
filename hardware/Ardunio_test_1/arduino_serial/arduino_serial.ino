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
  Serial.begin(9600);
  
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
  if (Serial.available() > 0) {
    byte cmd = Serial.read();

    if (cmd == 0x01) { // w
      
      analogWrite(motor1PWM, 50);
      analogWrite(motor2PWM, 50);
      analogWrite(motor3PWM, 50);

      digitalWrite(motor1IN1, HIGH); // clockwise
      digitalWrite(motor1IN2, LOW);
      digitalWrite(motor2IN1, LOW); // counter clockwise
      digitalWrite(motor2IN2, HIGH);
      digitalWrite(motor3IN4, LOW); // off
      digitalWrite(motor3IN3, LOW);
    }
    else if (cmd == 0x02) { // s
      analogWrite(motor1PWM, 50);
      analogWrite(motor2PWM, 50);
      analogWrite(motor3PWM, 50);

      digitalWrite(motor1IN1, LOW);
      digitalWrite(motor1IN2, HIGH);
      digitalWrite(motor2IN1, HIGH);
      digitalWrite(motor2IN2, LOW);
      digitalWrite(motor3IN4, LOW);
      digitalWrite(motor3IN3, LOW);
    }
    else if (cmd == 0x03) { // a
      analogWrite(motor1PWM, 50);
      analogWrite(motor2PWM, 50);
      analogWrite(motor3PWM, 100);

      digitalWrite(motor1IN1, HIGH);
      digitalWrite(motor1IN2, LOW);
      digitalWrite(motor2IN1, HIGH);
      digitalWrite(motor2IN2, LOW);
      digitalWrite(motor3IN4, LOW);
      digitalWrite(motor3IN3, HIGH);
    }
    else if (cmd == 0x04) { // d
      analogWrite(motor1PWM, 50);
      analogWrite(motor2PWM, 50);
      analogWrite(motor3PWM, 100);

      digitalWrite(motor1IN1, LOW);
      digitalWrite(motor1IN2, HIGH);
      digitalWrite(motor2IN1, LOW);
      digitalWrite(motor2IN2, HIGH);
      digitalWrite(motor3IN4, HIGH);
      digitalWrite(motor3IN3, LOW);
    }
    else if (cmd == 0x05) { // q
      analogWrite(motor1PWM, 50);
      analogWrite(motor2PWM, 50);
      analogWrite(motor3PWM, 50);

      digitalWrite(motor1IN1, HIGH);
      digitalWrite(motor1IN2, LOW);
      digitalWrite(motor2IN1, HIGH);
      digitalWrite(motor2IN2, LOW);
      digitalWrite(motor3IN4, HIGH);
      digitalWrite(motor3IN3, LOW);
    }
    else if (cmd == 0x06) { // e
      analogWrite(motor1PWM, 50);
      analogWrite(motor2PWM, 50);
      analogWrite(motor3PWM, 50);

      digitalWrite(motor1IN1, LOW);
      digitalWrite(motor1IN2, HIGH);
      digitalWrite(motor2IN1, LOW);
      digitalWrite(motor2IN2, HIGH);
      digitalWrite(motor3IN4, LOW);
      digitalWrite(motor3IN3, HIGH);
    }
    else if (cmd == 0x00) {
      analogWrite(motor1PWM, 0);
      analogWrite(motor2PWM, 0);
      analogWrite(motor3PWM, 0);

      digitalWrite(motor1IN1, LOW);
      digitalWrite(motor1IN2, LOW);
      digitalWrite(motor2IN1, LOW);
      digitalWrite(motor2IN2, LOW);
      digitalWrite(motor3IN4, LOW);
      digitalWrite(motor3IN3, LOW);
    }
  }

}
