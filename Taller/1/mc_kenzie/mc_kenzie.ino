void setup() {
  Serial.begin(9600);

}

void loop() {
  int i=0;
  while(i<4){
    Serial.println(i);
    i=i+1;
  }
}
 

