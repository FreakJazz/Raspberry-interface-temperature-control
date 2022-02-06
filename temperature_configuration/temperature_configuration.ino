#include <Wire.h>  // Library which contains functions to have I2C Communication
#define SLAVE_ADDRESS 0x40 // Define the I2C address to Communicate to Uno

byte response[2]; // this data is sent to PI
volatile short val1_2, val3_4; // Global Declaration
const int pval1_2 =A3; //pin to which LDR is connected A0 is analog A0 pin  
const int pval3_4 =A2; //pin to which LDR is connected A0 is analog A0 pin  

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS); // this will begin I2C Connection with 0x40 address
  Wire.onRequest(sendData); // sendData is funtion called when Pi requests data
  pinMode(pval1_2,INPUT);
  pinMode(pval3_4,INPUT);
}
void sendData(){
  val1_2=analogRead(pval1_2);
  // Arduino returns 10bit data but we need to convert it to 8bit 
  val1_2=map(val1_2,0,1023,0,255);
  response[0]=(byte)val1_2;
  Wire.write(response,2); // return data to PI
  /*val3_4=analogRead(pval3_4);
  // Arduino returns 10bit data but we need to convert it to 8bit 
  val3_4=map(val3_4,0,1023,0,255);
  response[0]=(byte)val3_4;
  Wire.write(response,2); // return data to PI*/
  Serial.println("ok");
}
void loop() {
  
  delay(30000);
}

