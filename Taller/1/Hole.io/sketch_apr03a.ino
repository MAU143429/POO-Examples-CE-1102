int pinLed1 = 2;
int pinLed2 = 3;
int pinLed3 = 4;

int pinLDR=0;

int valorLDR=0;
void setup() {
pinMode(pinLed1, OUTPUT);
pinMode(pinLed2, OUTPUT);
pinMode(pinLed3, OUTPUT);

  Serial.begin(9600);//Puerto Serial
}



void loop() {
 valorLDR= analogRead(pinLDR);
 Serial.println(valorLDR);
 if(valorLDR > 256 and valorLDR<512){
  digitalWrite(pinLed1,HIGH);
  digitalWrite(pinLed2,LOW);
  digitalWrite(pinLed3,LOW);
}
if(valorLDR > 512 and valorLDR<768){
  digitalWrite(pinLed1,HIGH);
  digitalWrite(pinLed2,HIGH);
  digitalWrite(pinLed3,LOW);

}

if(valorLDR <768){
  digitalWrite(pinLed1,HIGH);
  digitalWrite(pinLed2,HIGH);
  digitalWrite(pinLed3,HIGH);
}delay(500);

}
