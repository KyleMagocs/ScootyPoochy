

const int p1pad = A5;  // Analog input pin that the potentiometer is attached to
const int p2pad = A7;
const int p1pot = A2;
const int p2pot = A1;
const int p1butt = 3;
const int p2butt = 5;
const int led1 = 8;
const int led2 = 11;

int sensor1Value = 0;        // value read from the pot
int sensor2Value = 0;        // value read from the pot

void setup() {
  // initialize serial communications at 9600 bps:
//  Serial.begin(9600);
  pinMode(p1pad, INPUT_PULLUP);
  pinMode(p2pad, INPUT_PULLUP);
  pinMode(p1butt, INPUT_PULLUP);
  pinMode(p2butt, INPUT_PULLUP);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);

//  digitalWrite(led1, HIGH);
//  digitalWrite(led2, HIGH);
}

void loop() {
  // read the analog in value:
  sensor1Value = analogRead(p1pad);
  float cutoff1 = ((float)analogRead(p1pot) / 1024.0) * 100;
  
  sensor2Value = analogRead(p2pad);
  float cutoff2 = ((float)analogRead(p2pot) / 1024.0) * 100;
//  
//  Serial.print("pot1 = ");
//  Serial.print(analogRead(p1pot));
//  Serial.print("  |  cutoff1 = ");
//  Serial.print(cutoff1);
//  Serial.print("  |  sensor1 = ");
//  Serial.println(sensor1Value);
//
//  Serial.print("pot2 = ");
//  Serial.print(analogRead(p2pot));
//  Serial.print("  |  cutoff2 = ");
//  Serial.print(cutoff2);
//  Serial.print("  |  sensor2 = ");
//  Serial.println(sensor2Value);
  
  if (sensor1Value < cutoff1 || digitalRead(p1butt) == LOW) {
    digitalWrite(led1, HIGH);
    Keyboard.print('f');
  }
  else{
    digitalWrite(led1, LOW);
  }

  if (sensor2Value < cutoff2  || digitalRead(p2butt) == LOW) {
    digitalWrite(led2, HIGH);
    Keyboard.print('j');
  }
  else{
    digitalWrite(led2, LOW);
  }
  delay(10);
}
// 
