unsigned int rev(unsigned int in)
{
	unsigned int i, ret = 0;
	short b[8];

	for(i=0; i<8; i++) b[i] = 0;

	for(i=0; i<8; i++)
	{
		b[i] = in % 2;
		in >>= 1;
	}

	for(i=0; i<8; i++)
	{
		ret <<= 1;
		ret += b[i];
	}

	return ret;
}

int main()
{
	OS_PowerOnDriverInitial();

	// Setting for 7LED select
	GPIO_PTA_DIR = 0x0000;
	GPIO_PTA_CFG = 0x0000;

	// Setting for 7LED number
	GPIO_PTD_DIR = 0x0000;
	GPIO_PTD_CFG = 0x0000;

	// Setting  for Dip Switch
	GPIO_PTC_DIR = 0xFFFF;
	GPIO_PTC_CFG = 0x0000;
	GPIO_PTC_FS = 0x0000;
	GPIO_PTC_PADINSEL = 0x0000;

	// 16 LED, 0/1 = on/off
	GPIO_PTB_DIR = 0x0000;
	GPIO_PTB_CFG = 0xFFFF;

	unsigned int index_7LED[8] = {Digit_1, Digit_2, Digit_3, Digit_4, Digit_5, Digit_6, Digit_7, Digit_8};
	unsigned int index_7LED_NUM[17] = {Number_0, Number_1, Number_2, Number_3, Number_4, Number_5, Number_6, Number_7,
						Number_8, Number_9, Number_A, Number_b, Number_C, Number_d, Number_E, Number_F, Number_Dot};

	unsigned int tmp = 0;
	unsigned int i;

	
	
	// LED
	tmp = (GPIO_PTC_PADIN >> 2) & 0xFF;
	tmp = rev(tmp);
	GPIO_PTB_GPIO = tmp = (~tmp << 8) | tmp;

	for(i=0; i<16; i++)
	{
		tmp = ((tmp >> 1) | (tmp << 15)) & 0xFFFF;
		GPIO_PTB_GPIO = tmp;
		delay1(150000);
	}



	// 7seg
	tmp = (GPIO_PTC_PADIN >> 2) & 0xFF;
	unsigned int a = (tmp >> 4) & 0xF,
			 b = tmp & 0xF;

	unsigned int a1 = a / 10,
			a2 = a % 10,
			b1 = b / 10,
			b2 = b % 10;

	unsigned int cnt = 11, clock = 0;

	while(1)
	{
		if(a1 != 0)
		{
			GPIO_PTA_GPIO = index_7LED[3];
			GPIO_PTD_GPIO = index_7LED_NUM[a1];
			delay1(1000);
		}

		GPIO_PTA_GPIO = index_7LED[2];
		GPIO_PTD_GPIO = index_7LED_NUM[a2];
		delay1(1000);

		if(b1 != 0)
		{
			GPIO_PTA_GPIO = index_7LED[1];
			GPIO_PTD_GPIO = index_7LED_NUM[b1];
			delay1(1000);
		}

		GPIO_PTA_GPIO = index_7LED[0];
		GPIO_PTD_GPIO = index_7LED_NUM[b2];
		delay1(1000);

		unsigned int ans = a * b * abs(a - b);
		unsigned int ans_digit[4];

		ans_digit[0] = ans / 1000;
		ans_digit[1] = (ans % 1000) / 100;
		ans_digit[2] = (ans % 100) / 10;
		ans_digit[3] = ans % 10;


		for(i=0; i<4; i++)
		{
			if(cnt - i - 1 < 8)
			{
				if(i < 3 && ans_digit[i] != 0)
				{
					GPIO_PTA_GPIO = index_7LED[cnt - i - 1];
					GPIO_PTD_GPIO = index_7LED_NUM[ans_digit[i]];
					delay1(1000);
				}
				else if(i == 3)
				{
					GPIO_PTA_GPIO = index_7LED[cnt - i - 1];
					GPIO_PTD_GPIO = index_7LED_NUM[ans_digit[i]];
					delay1(1000);
				}
			}
		}

		if(clock > 200 && cnt > 8)
		{
			cnt--;
			clock = 0;
		}

		clock++;
	}

	return 0;
}
