#include <cvzone.h>

SerialData serialData(1,1);
int valsRec[2];

void setup() {
  serialData.begin();
 pinMode(13,OUTPUT);
 
}

void loop() {
  serialData.Get(valsRec);
  digitalWrite(13,valsRec[0]);
  digitalWrite(12,valsRec[1]);
  delay(10);
}
