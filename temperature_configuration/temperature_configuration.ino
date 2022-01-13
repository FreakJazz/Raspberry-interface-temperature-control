
int val1_2 = A3;     // potentiometer wiper (middle terminal) connected to analog pin 3
int val3_4 = A4;     // outside leads to ground and +5V
float temp1_2 = 0;  // variable to store the value read
float temp3_4 = 0;
int histeresis; // Banda de histeresis
int histe = 3;      // Valor final histeresis
float umbralbajo=0; // Umbral bajo de histeresis 
float umbralalto=0; // Umbral alto de histeresis


void setup() {
  Serial.begin(9600);           //  setup serial
  pinMode(6, OUTPUT);
  pinMode(7,OUTPUT);
  umbralbajo=setpoint-histe;
  umbralalto=setpoint+histe;
}

void loop() {
  temp1_2 = analogRead(val1_2);  // read the input pin
  temp1_2 = (5*temp1_2)/1023;
  temp1_2 = 23.07*temp1_2-18.46;
  // tpt100=8*vpt100+20;

  if temp
  
  
  Serial.println(temp1_2);          // debug value
  
  temp3_4 = analogRead(val3_4);  // read the input pin
  temp3_4 = (5*temp3_4)/1023;
  temp3_4 = 23.07*temp3_4-18.46;
  Serial.println(temp3_4);          // debug value
  delay(1000);
}

