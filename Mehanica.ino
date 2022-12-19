char* mex_dat[2] = {"UltraSonic", "GerconData"};

void mex(){
  state = 0;
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("vibor datchika");
  lcd.setCursor(0,1);
  lcd.print(mex_dat[state]);
  while(true){
    while(digitalRead(r4) == 0)
        {flag = 1; delay(50);}
    if (flag == 1)
        {flag = 0;
     if (state == 0)
     state = 1;
     else
        state--;
    lcd.setCursor(0,1);
    lcd.print(mex_dat[state]);
    }
    while(digitalRead(r2) == 0)
          {flag = 1; delay(50);}
        if (flag == 1)
        {
          flag = 0;
          state = (state + 1)% 2;
          lcd.setCursor(0,1);
          lcd.print(mex_dat[state]);
        }
    
    while(digitalRead(r1) == 0)
          {flag = 1; delay(50);}
        if (flag == 1)
        {flag = 0;
        break;}
  }
    switch(state){
      case 0:
        US_data();
        break;
      case 1:
        GC_data();
    }
      lcd.setCursor(0,0);
      lcd.print("S,cm");
      lcd.setCursor(0,1);
      lcd.print("t, c");
      for(int i = 0; i < 2; i++)
           {for(int j = 0; j < counter; j++)
              {Serial.print(value[i][j]);
               Serial.print(" ");}
            Serial.println();}
    }
 
  void US_data(){
    lcd.clear();
    digitalWrite(12,HIGH);
    lcd.setCursor(0,0);
    lcd.print("Start");
    while(true)
                {
                 while (digitalRead(r1) == 0){
                     flag = 1; delay(50);}
                 if (flag == 1){
                    flag = 0;
                    break;} }
    digitalWrite(12,LOW);
    lcd.setCursor(0,0);
    lcd.print("Progressing...");
    int duration, cm;
    while(true){
      digitalWrite(Trig,LOW);
      delayMicroseconds(2);
      digitalWrite(Trig,HIGH);
      delayMicroseconds(10);
      digitalWrite(Trig,LOW);
      duration = pulseIn(Echo,HIGH);
      cm = duration/58;
      value[0][counter] = cm;
      value[1][counter] = counter + 1;
      delay(100);
      counter++;
      if(counter > 19)
        break;      
  }
  lcd.clear();
  }

void GC_data(){
    lcd.clear();
    for(int i=0; i<4; i++){
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Vvedite datchik");
      lcd.print(i+1);
      lcd.setCursor(0, 1);
      digitalWrite(c4, HIGH);
     while(true){
     for(int c = 0; c < 2; c++)
      {
        digitalWrite(c+6, LOW);
        for(int r = 0; r < 4; r++)
        {
          while(digitalRead(5-r) == 0) 
            {delay(50);
            flag = 1;}
          if(flag == 1)
            {
              flag = 0;
              x = x*10 + (4*c + r + 1);
              if( x > 99)
                x = 0;
              lcd.setCursor(0, 1);
              if (x < 10)
                {lcd.print(" ");
                lcd.print(x);}
              else
                lcd.print(x);  
            }
          
        } 
       digitalWrite(c + 6, HIGH); 
      }
      digitalWrite(c3, LOW);
        for(int r = 0; r < 2; r++)
        {
          while(digitalRead(3-r) == 0) 
            {delay(50);
            flag = 1;}
          if(flag == 1)
            {
              flag = 0;
              x = x * 10;
              if(r == 0)
                x = x + 9;
              if( x > 99)
                x = 0;
              lcd.setCursor(0, 1);
              if (x < 10)
                {lcd.print(" ");
                lcd.print(x);}
              else
                lcd.print(x);  
            }
          
        } 
       digitalWrite(c3, HIGH);
      digitalWrite(c4, LOW); 
      while (digitalRead(r1) == 0){
        flag = 1;
        delay(50);}
      digitalWrite(c4, HIGH);
      if (flag == 1){
        flag = 0;
        value[0][i] = x;
        x = 0;
        break;} 
     }
    }
    lcd.clear();
    digitalWrite(12,HIGH);
    lcd.setCursor(0,0);
    lcd.print("Start");
    digitalWrite(c4, LOW);
    while(true)
                {
                 while (digitalRead(r1) == 0){
                     flag = 1; delay(50);}
                 if (flag == 1){
                    flag = 0;
                    break;} }
    digitalWrite(12,LOW);
    lcd.clear();
    long int time_start = millis()/100;
    flag = 0;
    while(true)
        {if (flag == 0 && digitalRead(A1) == 0)
            {flag = 1;
            value[1][counter] = millis()/100 - time_start;
            Serial.println(value[1][counter]);
            counter++;
            delay(20);}
         if (digitalRead(A1) == 1)
            flag = 0;
         if ((millis()/100 - time_start) > 50)
            {for(int i = 0; i < 4; i++)
                value[1][i] = 0;
             counter = 0;
             lcd.setCursor(0, 1);
             lcd.print("Restart");
             while(true)
                {
                 while (digitalRead(r1) == 0){
                     flag = 1; delay(50);}
      
                if (flag == 1){
                    flag = 0;
                    lcd.setCursor(0, 1);
                    lcd.print("         ");
                    time_start = millis()/100;
                    break;} }
            }
         if(counter > 3)
            break;
          }
    }
