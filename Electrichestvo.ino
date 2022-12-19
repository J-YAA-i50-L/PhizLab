void elek(){
lcd.clear();
state = 0;
counter = 0;
lcd.setCursor(0,0);
lcd.print("soberite skhemu");
lcd.setCursor(0,1);
lcd.print("start");
while(true){
  while(digitalRead(r1) == 0)
     {flag = 1; delay(50);}
  if (flag == 1)
     {flag = 0;break;}
  delay(50);}
lcd.clear();
lcd.setCursor(0,0);
lcd.print("V, B");
lcd.setCursor(0,1);
lcd.print("I,mA");
lcd.setCursor(12,1);
lcd.print(save_exit[state]);
while(true)
  {int v_value, i_value, v, i;
  v_value = analogRead(A0);
  i_value = analogRead(A1);
  v = map(v_value,0 ,1024 ,0 ,500);
  i = map(i_value,0 ,1024 ,0 ,500);
  lcd.setCursor(5,0);
  if (v < 10){
      lcd.print("  ");
      lcd.print(v);}
  else if (v < 100){
      lcd.print(" ");
      lcd.print(v);}
  else
      lcd.print(v);

  lcd.setCursor(5,1);
  if (i < 10){
      lcd.print("  ");
      lcd.print(i);}
  else if (i < 100){
      lcd.print(" ");
      lcd.print(i);}
  else
    lcd.print(i);
  Serial.print(v);
  Serial.print(" ");
  Serial.println(i);
  while(digitalRead(r4) == 0)
      {flag = 1; delay(50);}
  if (flag == 1)
      {flag = 0;
      if (state == 0)
          state = 1;
      else
          state--;
      lcd.setCursor(12,1);
      lcd.print(save_exit[state]);
      }
  while(digitalRead(r2) == 0)
      {flag = 1; delay(50);}
  if (flag == 1)
      {flag = 0;
      state = (state + 1) % 2;
      lcd.setCursor(12,1);
      lcd.print(save_exit[state]);}
  while(digitalRead(r1) == 0)
      {flag = 1; delay(50);}
  if (flag == 1)
      {flag = 0;
      if(state == 0){
        value[0][counter] = v;
        value[1][counter] = i;
        counter ++;
        }
      else
        break;
      }
  if (counter > 9)
    break;
  delay(100);
  }
lcd.setCursor(12,1);
  lcd.print("    ");
}
