#include <Servo.h>
#define IN1 4
#define IN2 3
#define IN3 6
#define IN4 5

Servo s1;
Servo s2;

void test_dc_run()
{
  digitalWrite(IN1, LOW);
  analogWrite(IN2,150);
}
void test_dc_stop()
{
  digitalWrite(IN1, LOW);
  analogWrite(IN2, LOW);
}
void setup() 
{
  Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  pinMode(LED_BUILTIN, OUTPUT);
  s1.attach(9);
  s2.attach(10);
}

void loop() 
{
  s1.write(180);
  s2.write(0); 
  test_dc_run();

    if (Serial.available() > 0) 
    {
      String data = Serial.readStringUntil('\n');
      Serial.print("san pham loai: ");
      Serial.println(data);
      
      if (data == "1") 
      {
          test_dc_run();
          s1.write(135);
          s2.write(0);
          delay(10000);
          s1.write(180);
          s2.write(0);
          data = Serial.readString();
          
      }
     else if (data == "2")
      {
          test_dc_run();
          s1.write(180);
          s2.write(60);
          delay(10000);
          s1.write(180);
          s2.write(0);         
         data = Serial.readString();
      } 
      else 
      {
        s1.write(180);
        s2.write(0);
        data = Serial.readString();
      }
      
  } 

}