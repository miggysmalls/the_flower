#include <Servo.h>

#define trigPin 8
#define echoPin 9
#define redLED 2
#define yellowLED 4
#define greenLED 7
#define flowerWake 10


Servo waken;
long duration;
float distanceCM;
float distanceInch;

void setup() {
waken.attach(flowerWake);
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
pinMode(redLED, OUTPUT);
pinMode(yellowLED, OUTPUT);
pinMode(greenLED, OUTPUT);
Serial.begin(9600); 
}

void loop() {
digitalWrite(trigPin, LOW);
delayMicroseconds(2);

digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

duration = pulseIn(echoPin, HIGH);

distanceCM = duration * 0.034 /2;
distanceInch = duration * 0.0133 /2;

Serial.print("Distance: ");
Serial.print(distanceCM);
Serial.print("  CM  -  ");

Serial.print(distanceInch);
Serial.println("  Inches");

if (distanceCM >= 100) {
  waken.write(0);
  digitalWrite(greenLED, HIGH);
  digitalWrite(yellowLED, LOW);
  digitalWrite(redLED, LOW);
}
else if (distanceCM < 100 &&  distanceCM > 50) {  
  waken.write(90);
  digitalWrite(greenLED, LOW);
  digitalWrite(yellowLED, HIGH);
  digitalWrite(redLED, LOW);
}
else {
  waken.write(180);
  digitalWrite(greenLED, LOW);
  digitalWrite(yellowLED, LOW);
  digitalWrite(redLED, HIGH);  
}

delay(1000);
}
