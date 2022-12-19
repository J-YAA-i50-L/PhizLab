void rez(){
  
  for(int j = 0; j < 3; j++){
    lcd.setCursor((5 + j * 4),0);
    lcd.print(value[0][j]);
    lcd.setCursor((5+ j * 4),1);
    lcd.print(value[1][j]);}
  state = 0;
  while(true){
    while(digitalRead(r4) == 0)
      {flag = 1; delay(50);}
    if (flag == 1)
      {flag = 0;
      if (state == 0)
          state = 0;
      else
          state--;
      for(int j = 0; j < 3; j++){
        lcd.setCursor((5 + j * 4),0);
        if(value[0][state + j] < 10){
          lcd.print("  ");
          lcd.print(value[0][state + j]);}
        else if (value[0][state + j] < 100){
          lcd.print(" ");
          lcd.print(value[0][state + j]);}
       else
          lcd.print(value[0][state + j]);
       lcd.setCursor((5+ j * 4),1);
       if(value[1][state + j] < 10){
          lcd.print("  ");
          lcd.print(value[1][state + j]);}
       else if (value[1][state + j] < 100){
          lcd.print(" ");
          lcd.print(value[1][state + j]);}
       else
          lcd.print(value[1][state + j]);}
      }
    while(digitalRead(r2) == 0)
        {flag = 1; delay(50);}
    if (flag == 1)
      {flag = 0;
      if (state == counter - 3)
         state = counter - 3;
      else
         state++;
      for(int j = 0; j < 3; j++){
        lcd.setCursor((5 + j * 4),0);
        if(value[0][state + j] < 10){
          lcd.print("  ");
          lcd.print(value[0][state + j]);}
        else if (value[0][state + j] < 100){
          lcd.print(" ");
          lcd.print(value[0][state + j]);}
        else
          lcd.print(value[0][state + j]);
        lcd.setCursor((5+ j * 4),1);
        if(value[1][state + j] < 10){
          lcd.print("  ");
          lcd.print(value[1][state + j]);}
        else if (value[1][state + j] < 100){
          lcd.print(" ");
          lcd.print(value[1][state + j]);}
        else
          lcd.print(value[1][state + j]);}
      }
    }
  }
