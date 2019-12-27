#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int bin[32];

void printBinary(unsigned int value)
{
	memset(bin, 0, sizeof(bin));

	printf("%u = ", value);
	for(int i=0; i<32; i++)
	{
		unsigned int tmp = value;
		tmp <<= i;
		tmp >>= 31;
		if((i+1) % 8 == 0) printf("%d ", bin[i] = tmp&0b1);
		else printf("%d", bin[i] = tmp&0b1);
	}
	printf("\n");
}

int main(int argc, char const *argv[])
{
	unsigned int num;

	while(~scanf("%u", &num))
	{
		printf("Before bits are reversed:\n");
		printBinary(num);

		unsigned int rev = 0;

		for(int i=31; i>=0; i--)
		{
			if(bin[i] == 1) rev += 1;
			if(i > 0) rev <<= 1;
		}

		printf("\nAfter bits are reversed:\n");
		printBinary(rev);
	}

	return 0;
}