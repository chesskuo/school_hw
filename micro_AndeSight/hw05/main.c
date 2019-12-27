void Display_1Line(unsigned int WordValue)
{
  // char ABC[]={'A','b','C','d','E','f','G','h'};
  char ABC[] = "406262187";
  char i=0;
  WriteIns(0x38);  //FUNCTION SET
  WriteIns(0x0E);  //DISPLAY CONTROL
  WriteIns(0x06);  //SET INPUT MODE
  for(i=0;i<WordValue;i++)
  {
    WriteData(ABC[i]);
    delay1(300000);
  }
}

void Display_2Line(int WordValue)
{
  //char ABCD[]={'A','N','D','E','S'};
  char ABCD[]="406262462";
  char i;
  WriteIns(0x38);  //FUNCTION SET
  WriteIns(0x0E);  //DISPLAY CONTROL
  WriteIns(0x06);  //SET INPUT MODE
  WriteIns(0xC0);  //2-LINE DD RAM SET Address
  for(i=0;i<WordValue;i++)
  {
    WriteData(ABCD[i]);
    delay1(300000);
  }
}



int main()
{
	OS_PowerOnDriverInitial();
	InitialLCD();



	unsigned int i;
	unsigned int tmp;
	unsigned int stat = 0;

	while(1)
	{
		key = 0xFF;
		GPIO_PTA_DIR = 0x0FF0;
		GPIO_PTA_CFG = 0x0000;
		for (col=0; col<4; col++)
		{
			GPIO_PTA_BS = 0x000F;
			GPIO_PTA_BR = 0x0000 | (1 << col);
			tmp = ((~GPIO_PTA_PADIN) & 0xFF0) >> 4;
			if (tmp > 0)
			{
				if (tmp & 0x1)
					key = 0*4 + col;
				else if (tmp & 0x2 && col < 3)
					key = 1*4 + col;
				break;
			}
		}

		if(key != 0xFF)
		{
			if(key == 0x0)
			{
				Display_1Line(9);
				delay1(1000000);
			}
			else if(key == 0x1)
			{
				Display_2Line(9);
				delay1(1000000);
			}
			else if(key == 0x2)
			{
				WriteIns(0x18);
				delay1(20000);
			}
			else if(key == 0x3)
			{
				WriteIns(0x1C);
				delay1(20000);
			}
			else if(key == 0x4) WriteIns(0x01);  // clear buffer
			else if(key == 0x5) WriteIns(0x02);  // return home
			else if(key == 0x6)
			{
				if(stat == 0)
				{
					WriteIns(0x0E);
					stat = 1;
				}
				else
				{
					WriteIns(0x0C);
					stat = 0;
				}
			}
		}
	}

	return 0;
}
