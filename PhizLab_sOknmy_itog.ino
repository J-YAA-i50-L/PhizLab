#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
#define Echo 14
#define Trig 13
#define c4 9
#define c3 8
#define c2 7
#define c1 6
#define r4 5
#define r2 3
#define r1 2
char* razdel[3] = {"MEXANIKA", "MKT", "ELEKTRICHESTVO"};
char* save_exit[2] = {"save", "exit"};
int value[2][20];
int flag = 0;
int state = 0;
int x = 0;
int counter;

void setup() {
  pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(A0,INPUT);
  pinMode(A1,INPUT);
  pinMode(A2,INPUT);
  Serial.begin(9600);
  for(int i = 0; i < 4; i++)
    {pinMode(i+2,INPUT_PULLUP);
    pinMode(i+6,OUTPUT);
    digitalWrite(i+6,HIGH);}
  lcd.init(); 
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Welcome to PhLab");
  delay(2000);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Vyberite razdel");
  lcd.setCursor(0,1);
  lcd.print(razdel[state]);
  digitalWrite(c4,LOW);
  while (true)
    {while(digitalRead(r4) == 0)
        {delay(50); flag = 1;}
    if (flag == 1)
        {flag = 0;   
        if (state == 0)
           state = 2;
        else
           state--;
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.print("Vyberite razdel");
        lcd.setCursor(0,1); 
        lcd.print(razdel[state]);
        }
     while(digitalRead(r2) == 0)
        {delay(50); flag = 1;}
     if (flag == 1)
        {flag = 0;
        state = (state + 1)% 3;
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.print("Vyberite razdel");
        lcd.setCursor(0,1); 
        lcd.print(razdel[state]);
         }
  
    while(digitalRead(r1) == 0)
        {delay(50); flag = 1;}
    if (flag == 1)
        {flag = 0; break;}
    }
  switch(state)
    {case 0:
      mex();
      break;
    case 1:
      mkt();
      break;
    case 2:
      elek();
      break;
    }
  rez();
  }

void loop() {
  }
  
