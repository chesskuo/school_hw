#include <stdio.h>
#include <stdlib.h>

void printBinary(unsigned int in)
{
	char bin[] = "01";
	unsigned int tmp;

	for(int i=0; i<32; i++)
	{
		tmp = in;
		tmp <<= i;
		tmp >>= 31;
		printf("%c", bin[tmp&0b1]);
	}
	printf("\n");
}

void printOctal(unsigned int in)
{
	char oct[] = "01234567";
	unsigned int tmp;

	printf("0");
	for(int i=1; i<32; i+=3)
	{
		tmp = in;
		if(i == 1) tmp >>= 1;
		else tmp <<= i-2;
		tmp >>= 29;
		printf("%c", oct[tmp&07]);
	}
	printf("\n");
}

void printHexidecimal(unsigned int in)
{
	char hex[] = "0123456789ABCDEF";
	unsigned int tmp;

	printf("0x");
	for(int i=3; i<32; i+=4)
	{
		tmp = in;
		tmp <<= i-3;
		tmp >>= 28;
		printf("%c", hex[tmp&0xF]);
	}
	printf("\n");
}

int main(int argc, char const *argv[])
{
	unsigned int num;
	int cas = 1;

	while(scanf("%u", &num) != EOF)
	{
		printf("Case %d: %u\n", cas++, num);
		printBinary(num);
		printOctal(num);
		printHexidecimal(num);
	}

	return 0;
}