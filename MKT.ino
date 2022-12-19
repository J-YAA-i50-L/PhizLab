char* mkt_dat[3] = {"P and V", "P and T", "V and T"};
float mr[29] = {181.70, 133.30, 98.88, 74.10, 56.06, 42.80, 32.96, 25.58, 20.00, 15.76, 12.51, 10.00, 8.048, 6.518, 5.312,
                4.354, 3.588, 2.974, 2.476, 2.072, 1.743, 1.473, 1.250, 1.065, 0.911, 0.782, 0.6744, 0.5836, 0.5066};
int mt[29];
void mkt(){
  state = 0;
  for(int j=0; j<29; j++){
      mt[j]=-30+(j*5);}
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("vibor datchika");
  lcd.setCursor(0,1);
  lcd.print(mkt_dat[state]);
  while(true){
     while(digitalRead(r4) == 0)
      {flag = 1; delay(50);}
    if (flag == 1)
        {flag = 0;
        if (state == 0)
          state = 2;
        else
          state--;
        lcd.setCursor(0,1);
        lcd.print(mkt_dat[state]);
        }
    while(digitalRead(r2) == 0)
      {flag = 1; delay(50);}
    if (flag == 1)
        {flag = 0;
        state = (state + 1)% 3;
        lcd.setCursor(0,1);
        lcd.print(mkt_dat[state]);
        }

    while(digitalRead(r1) == 0)
        {flag = 1; delay(50);}
    if (flag == 1)
    {flag = 0;
    break;}
  }
switch(state){
  case 0:
    PV_data();
    break;
  case 1:
    PT_data();
    break;
  case 2:
    VT_data();
  }

}

void PV_data(){
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Pmrs");
  lcd.setCursor(0,1);
  lcd.print("V,ml");
  state = 0;
  lcd.setCursor(12,1);
  lcd.print(save_exit[state]);
  while(true)
    {int p_value, v_value, p, v;
    p_value = analogRead(A0);
    v_value = analogRead(A1);
    p = map(p_value,110 ,1000 ,580,880);
    v = map(v_value,500 ,1023,3,18);
    lcd.setCursor(5,0);
    lcd.print(p);
    lcd.setCursor(5,1);
    if(v < 10){
        lcd.print("  ");
        lcd.print(v);}
    else if (v < 100){
        lcd.print(" ");
        lcd.print(v);}
    else
        lcd.print(v);
    Serial.print(p);
    Serial.print(" ");
    Serial.println(v);
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
        value[0][counter] = p;
        value[1][counter] = v;
        counter++;
        }
      else
      break;}
    delay(100);
    }
  lcd.setCursor(12,1);
  lcd.print("    ");
    }


void PT_data(){
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Pmrs");
  lcd.setCursor(0,1);
  lcd.print("T, K");
  state = 0;
  lcd.setCursor(12,1);
  lcd.print(save_exit[state]);
  while(true)
    {int p_value, t_value, p, t;
    float q, z, temp;
    p_value = analogRead(A0);
    t_value = analogRead(A2);
    p = map(p_value,110 ,1000 ,580 ,880);
    z = map(t_value,0,1023,0,5000);
    z = z / 1000;
    q=z*10.0/(5.0-z);
    for(int j=0; j<28; j++){
      if(q < mr[j] && q >= mr[j+1]){
        temp = map(q*1000, mr[j]*1000, mr[j+1]*1000, mt[j]*100, mt[j+1]*100);
        temp = temp/100;
        j = 28;}
      }
    t = int(temp) + 273;
    lcd.setCursor(5,0);
    lcd.print(p);
    lcd.setCursor(5,1);
    lcd.print(t);
    Serial.print(p);
    Serial.print(" ");
    Serial.println(t);
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
        value[0][counter] = p;
        value[1][counter] = t;
        counter ++;}
      else
        break;}
    delay(100);
    }
  lcd.setCursor(12,1);
  lcd.print("    ");
  }

void VT_data(){
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("V,ml");
  lcd.setCursor(0,1);
  lcd.print("T, K");
  state = 0;
  lcd.setCursor(12,1);
  lcd.print(save_exit[state]);
  while(true)
    {int v_value, t_value, v, t;
    float q, z, temp;
    v_value = analogRead(A1);
    t_value = analogRead(A2);
    v = map(v_value,500 ,1023,3,18);
    z = map(t_value,0,1023,0,5000);
    z = z / 1000;
    q=z*10.0/(5.0-z);
    for(int j=0; j<28; j++){
      if(q < mr[j] && q >= mr[j+1]){
        temp = map(q*1000, mr[j]*1000, mr[j+1]*1000, mt[j]*100, mt[j+1]*100);
        temp = temp/100;
        j = 28;}}
    t = int(temp) + 273;
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
    lcd.print(t);
    Serial.print(v);
    Serial.print(" ");
    Serial.println(t);
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
        value[1][counter] = t;
        counter ++;}
      else
        break;}
    delay(100);
    }
   lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("V,ml");
  lcd.setCursor(0,1);
  lcd.print("T, K");
  }
