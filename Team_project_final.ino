#include<Servo.h>
Servo bottom, mid, pick, pick2;

void setup() {
  Serial.begin(9600);
  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
  
  bottom.attach(3);
  mid.attach(5);
  pick.attach(6);
  pick2.attach(9);
  
  bottom.write(90);
  mid.write(90);
  pick.write(50);
  pick2.write(70);


  // put your setup code here, to run once:

}

  int b_angle = 90;
  int m_angle = 90;
  int pick_angle = 50;
  int pickr_angle = 70;
  bool count = 0;
  int readinfo;
    
void loop() {

  if(Serial.available())
  {
    readinfo = Serial.read();
    count = 1;
  }

  while(count == 1)
  {
    if(Serial.available())
    {
      Serial.read();
    }
    
    if(readinfo == 1)
    {
      bottom.write(b_angle);
      delay(50);
      b_angle += 1;
    }

    if(readinfo == 2)
    {
      bottom.write(b_angle);
      delay(50);
      b_angle -= 1;
    }
  
    if(readinfo == 3)
    {
      mid.write(m_angle);
      delay(50);
      m_angle += 1;
    }

    if(readinfo == 4)
    {
      mid.write(m_angle);
      delay(50);
      m_angle -= 1;
    }

    if(readinfo == 5)
    {
      pick.write(pick_angle);
      pick2.write(pickr_angle);
      pick_angle -= 1;
      pickr_angle += 1;
      delay(100);
    }

    if(readinfo == 6)
    {
      pick.write(pick_angle);
      pick2.write(pickr_angle);
      pick_angle += 1;
      pickr_angle -= 1;
      delay(100);
    }

    if(Serial.read() == 7)
    { 
      count = 0;
    }

    if(readinfo == 8)
    {
      b_angle = 90;
      m_angle = 90;
      pick_angle = 50;
      pickr_angle = 70;
      bottom.write(b_angle);
      mid.write(m_angle);
      pick.write(pick_angle);
      pick2.write(pickr_angle);
      delay(500);
      break;
    }

  }
  // put your main code here, to run repeatedly:

}
