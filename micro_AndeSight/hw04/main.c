int main()
{
	OS_PowerOnDriverInitial();

	GPIO_PTA_FS = 0x0000;
	GPIO_PTA_PADINSEL = 0x0000;

	// Setting for 7LED select
	GPIO_PTA_DIR = 0x0000;
	GPIO_PTA_CFG = 0x0000;
	GPIO_PTA_GPIO = Digit_8;
	// Setting for 7LED number
	GPIO_PTD_DIR = 0x0000;
	GPIO_PTD_CFG = 0x0000;
	GPIO_PTD_GPIO = Number_8 | Number_Dot;

	GPIO_PTC_FS = 0x0000;
	GPIO_PTC_PADINSEL = 0x0000;
	GPIO_PTC_DIR = 0xFFFF;
	GPIO_PTC_CFG = 0x0000;

	unsigned int col, i;
	unsigned int key;
	unsigned int index_7LED_NUM[17] = {Number_0, Number_1, Number_2, Number_3, Number_4, Number_5, Number_6, Number_7, Number_8, Number_9, Number_A, Number_b, Number_C, Number_d, Number_E, Number_F, Number_Dot};
	unsigned int index_7LED_Digit[8] = {Digit_8, Digit_7, Digit_6, Digit_5, Digit_4, Digit_3, Digit_2, Digit_1};
	unsigned int num[8];
	unsigned int lock = 0, now = 0;
	unsigned int tmp = 0;
	int tmp2, sign = 0;
	char mode;

	for(i=0; i<8; i++) num[i] = 0;

	while(1)
	{
		key = 0xFF;
		GPIO_PTA_DIR = 0x0FF0;
		GPIO_PTA_CFG = 0x0000;
		for (col=0; col<4; col++)
		{
			GPIO_PTA_BS = 0x000F;
			GPIO_PTA_BR = 0x0000 | (1 << col);
			tmp = (GPIO_PTC_PADIN >> 2) & 0x1;
			if(tmp)
			{
				for(i=0; i<8; i++) num[i] = 0;
				lock = 0;
				now = 0;
				sign = 0;
			}

			tmp = ((~GPIO_PTA_PADIN) & 0xFF0) >> 4;
			if (tmp > 0)
			{
				if (tmp & 0x1)
					key = 0*4 + col;
				else if (tmp & 0x2)
					key = 1*4 + col;
				else if (tmp & 0x4 && col < 2)
					key = 2*4 + col;
				else if (tmp & 0x80)
					mode = '+';
				else if (tmp & 0x40)
					mode = '-';
				else if (tmp & 0x20)
					mode = '*';
				else if (tmp & 0x10)
					mode = '/';
				break;
			}
		}



		if (key != 0xFF)
		{
			if(lock == 0 && now < 4)
			{
				num[now++] = (key + 1) % 10;
				lock = 1;
			}

			if(now == 4) mode = key;
		}
		else lock = 0;



		if(now == 4)
		{
			switch(mode)
			{
				case '+':
					tmp2 = (num[0]*10 + num[1]) + (num[2]*10 + num[3]);
					num[4] = tmp2 / 1000; num[5] = (tmp2 % 1000) / 100; num[6] = (tmp2 % 100) / 10; num[7] = tmp2 % 10;
					now++;
					break;
				case '-':
					tmp2 = (num[0]*10 + num[1]) - (num[2]*10 + num[3]);
					if(tmp2 < 0)
					{
						tmp2 = 0 - tmp2;
						sign = 1;
					}
					num[4] = tmp2 / 1000; num[5] = (tmp2 % 1000) / 100; num[6] = (tmp2 % 100) / 10; num[7] = tmp2 % 10;
					now++;
					break;
				case '*':
					tmp2 = (num[0]*10 + num[1]) * (num[2]*10 + num[3]);
					num[4] = tmp2 / 1000; num[5] = (tmp2 % 1000) / 100; num[6] = (tmp2 % 100) / 10; num[7] = tmp2 % 10;
					now++;
					break;
				case '/':
					tmp2 = (num[0]*10 + num[1]) / (num[2]*10 + num[3]);
					num[4] = tmp2 / 1000; num[5] = (tmp2 % 1000) / 100; num[6] = (tmp2 % 100) / 10; num[7] = tmp2 % 10;
					now++;
					break;
			}
		}



		// number input
		for(i=0; i<4; i++)
		{
			if(i == 0 && num[i] == 0) continue;
			if(i == 2 && num[i] == 0) continue;

			GPIO_PTD_GPIO = index_7LED_NUM[num[i]];
			GPIO_PTA_GPIO = index_7LED_Digit[i];
			delay1(1000);
		}

		// result
		int check = 0;

		if(now == 5)
		{
			for(i=4; i<8; i++)
			{
				if(i != 7 && num[i] == 0 && check == 0)
				{
					if(sign && num[i+1])
					{
						GPIO_PTD_GPIO = 0x4040;
						GPIO_PTA_GPIO = index_7LED_Digit[i];
						delay1(1000);
					}
					continue;
				}

				check = 1;
				GPIO_PTD_GPIO = index_7LED_NUM[num[i]];
				GPIO_PTA_GPIO = index_7LED_Digit[i];
				delay1(1000);
			}
		}
	}

	return 0;
}
