int main()
{
	unsigned int tmp = 0;


	OS_PowerOnDriverInitial();


	DRV_Printf("================================================\r\n", 0);
	DRV_Printf("   ADP-WT58F2C9 DIP Switch (SW1) demo program   \r\n", 0);
	DRV_Printf("================================================\r\n", 0);


	DRV_Printf("DIP Switch (SW1) testing ...\r\n", 0);

	// Setting for 7LED select
	GPIO_PTA_DIR = 0x0000;
	GPIO_PTA_CFG = 0x0000;
	GPIO_PTA_GPIO = Digit_1;
	// Setting for 7LED number
	GPIO_PTD_DIR = 0x0000;
	GPIO_PTD_CFG = 0x0000;
	GPIO_PTD_GPIO = 0xFFFF;

	GPIO_PTC_FS = 0x0000;
	GPIO_PTC_PADINSEL = 0x0000;
	GPIO_PTC_DIR = 0xFFFF;
	GPIO_PTC_CFG = 0x0000;

	GPIO_PTA_GPIO = Digit_1;

	unsigned int digit[] = {Digit_1, Digit_2, Digit_3, Digit_4, Digit_5, Digit_6, Digit_7, Digit_8};

	unsigned int stu[2][8] = {{Number_4, Number_0, Number_6, Number_2, Number_6, Number_2, Number_1, Number_8},
								{Number_4, Number_0, Number_6, Number_2, Number_6, Number_2, Number_4, Number_6}};

	int i = 0,
		now = 1;

	unsigned long long int clock = 0;

	while(1)
	{
		tmp = (GPIO_PTC_PADIN >> 2) & 0x3;
		unsigned int tmp2 = now;

		switch(tmp)
		{
			case 0:
				GPIO_PTD_GPIO = 0x0;
				now = 1;
				break;
			case 1:
				for(i=0; i<now; i++)
				{
					GPIO_PTA_GPIO = digit[--tmp2];
					GPIO_PTD_GPIO = stu[0][i];
					delay1(1000);
				}
				break;
			case 2:
				for(i=7; i>=8-now; i--)
				{
					GPIO_PTA_GPIO = digit[7-(--tmp2)];
					GPIO_PTD_GPIO = stu[1][i];
					delay1(1000);
				}
				break;
			default:
				GPIO_PTD_GPIO = 0x0;
				now = 1;
				break;
		}

		if(now < 8 && clock > 100)
		{
			now++;
			clock = 0;
		}

		clock++;
	}


	DRV_Printf("================================================\r\n", 0);


	return 0;
}
