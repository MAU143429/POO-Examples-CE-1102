#define Clock D6
#define Data D5
#define ENA1 D7
#define ENA2 D8
byte re = 0b11111111;
byte d2 = 0b11111010;
byte d1 = 0b11110101;
byte df = 0b11110011;
byte tf = 0b11111100;



void DI() {
  shiftOut(ab, clk, LSBFIRST, re);
  delay(500);
  shiftOut(ab, clk, LSBFIRST, d1);
  delay(500);
  shiftOut(ab, clk, LSBFIRST, re);
  delay(500);
  shiftOut(ab, clk, LSBFIRST, d1);
  delay(500);

}

void DD() {
  shiftOut(ab, clk, LSBFIRST, re);
  delay(500);
  shiftOut(ab, clk, LSBFIRST, d2);
  delay(500);
  shiftOut(ab, clk, LSBFIRST, re);
  delay(500);
  shiftOut(ab, clk, LSBFIRST, d2);
  delay(500);
  
  
}

void DF() {
  shiftOut(ab, clk, LSBFIRST,df);
  delay(1);
  shiftOut(ab, clk, LSBFIRST, df);
  delay(1);
  shiftOut(ab, clk, LSBFIRST, df);
  delay(1);
  shiftOut(ab, clk, LSBFIRST, df);
  delay(1);
  
  
}

void TF() {
  shiftOut(ab, clk, LSBFIRST,tf);
  delay(1);
  shiftOut(ab, clk, LSBFIRST, tf);
  delay(1);
  shiftOut(ab, clk, LSBFIRST, tf);
  delay(1);
  shiftOut(ab, clk, LSBFIRST, tf);
  delay(1);
  
  
}



void setup() {
  //Serial.begin(115200);
  pinMode(Clock, OUTPUT);
  pinMode(Data, OUTPUT);
  pinMode(ENA1, OUTPUT);
  pinMode(ENA2, OUTPUT);
  digitalWrite(Clock, LOW);
  digitalWrite(Data, LOW);
  digitalWrite(ENA1, LOW);
  digitalWrite(ENA2, LOW);
  
}

void loop(){
  TF();
  

  }
