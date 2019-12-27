unsigned int morning;

void SetupRTCTime(void)
{
	unsigned int tyear[2] = {1, 9}, tmon = 10, tday[2] = { 3, 0}, tweek = 1;
	unsigned int thour[2] = {1, 2}, tmin[2] = { 5, 9 }, tsec[2] = {5, 8};

	// Initialize RTC (Real Time Clock)
	RTC_YEAR = (tyear[0] << 4) | tyear[1];      // fill in op
	RTC_MONTH =  tmon;
	RTC_DAY = (tday[0] << 4) | tday[1];         // fill in op
	RTC_WEEK = tweek;

	RTC_HOUR = (thour[0] << 4) | thour[1];
	RTC_MIN = (tmin[0] << 4) | tmin[1];
	RTC_SEC = (tsec[0] << 4) | tsec[1];
}

void DisplayTime(void)
{
	char week_array[7][4] = {"Sun","Mon","Tue","Wed","Thu","Fri","Sat"};
	int i;

	unsigned int year = RTC_YEAR, mon = RTC_MONTH, day = RTC_DAY;
	unsigned int hour = RTC_HOUR, min = RTC_MIN, sec = RTC_SEC;
	unsigned int week = RTC_WEEK;

	unsigned int tmp_hour[2] = {((hour >> 4) & 0xF), (hour & 0xF)};
	unsigned int tmp = tmp_hour[0]*10 + tmp_hour[1];

	if(tmp < 12)
	{
		morning = 1;
		if(tmp == 0) tmp = 12;
	}
	else
	{
		morning = 0;
		if(tmp > 12) tmp %= 12;
	}

	tmp_hour[0] = tmp / 10;
	tmp_hour[1] = tmp % 10;
	hour = (tmp_hour[0] << 4) | tmp_hour[1];

	SetCursor(0, 0x1); //WriteIns(0x8000); //STN LCM,第一列

	WriteData('2'); //字元"2"
	WriteData('0'); //字元"0"
	WriteData(((year >> 4) & 0x000F) + To_ASCII);
	WriteData((year & 0x000F) + To_ASCII);
	WriteData('/'); //":"符號

	WriteData(((mon & 0x000F) / 10) + To_ASCII);
	WriteData(((mon & 0x000F) % 10) + To_ASCII);
	WriteData('/'); //":"符號

	WriteData(((day >> 4) & 0x000F) + To_ASCII);
	WriteData((day & 0x000F) + To_ASCII);
	WriteData(' ');

	for(i=0;i<3;i++) WriteData(week_array[(int)week][i]);
	WriteData('.'); //"."符號



	SetCursor(1, 0x5); //WriteIns(0xC000); //STN LCM,第二列

	WriteData(((hour >> 4) & 0x000F) + To_ASCII);
	WriteData((hour & 0x000F) + To_ASCII);
	WriteData(':'); //":"符號

	WriteData(((min >> 4) & 0x000F) + To_ASCII);
	WriteData((min & 0x000F) + To_ASCII);
	WriteData(':'); //":"符號

	WriteData(((sec >> 4) & 0x000F) + To_ASCII);
	WriteData((sec & 0x000F) + To_ASCII);
	WriteData(' ');

	if(morning) WriteData('A');
	else WriteData('P');
	WriteData('M');
}

int main()
{
	OS_PowerOnDriverInitial();
	InitialLCD();
	InitialRTC();

	SetupRTCTime();	 // SetupRealTime4RTC();

	while(1) DisplayTime();

	return 0;
}
