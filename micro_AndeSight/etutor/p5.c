#include <stdio.h>
#include <stdlib.h>

void printBinary(unsigned int value)
{
	printf("%u = ", value);
	for(int i=0; i<32; i++)
	{
		unsigned int tmp = value;
		tmp <<= i;
		tmp >>= 31;
		if((i+1) % 8 == 0) printf("%d ", tmp&0b1);
		else printf("%d", tmp&0b1);
	}
	printf("\n");
}

int main(int argc, char const *argv[])
{
	unsigned int num;

	while(~scanf("%u", &num))
	{
		printf("The packed character representation is:\n");
		printBinary(num);
		printf("\n");

		unsigned int a = (num & 0xFF000000) >> 24,
					b = (num & 0x00FF0000) >> 16,
					c = (num & 0x0000FF00) >> 8,
					d = num & 0x000000FF;

		// printf("The unpacked characters are \'%c\' and \'%c\' and \'%c\' and \'%c\'\n", a, b, c, d);
		printBinary(a);
		printBinary(b);
		printBinary(c);
		printBinary(d);
	}

	return 0;
}