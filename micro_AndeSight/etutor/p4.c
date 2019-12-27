#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void displayBits(int value)
{
	printf("%u =", value);
	for(int i=0; i<32; i++)
	{
		unsigned int tmp = value;
		tmp <<= i;
		tmp >>= 31;
		if(i % 8 == 0) printf(" %d", tmp&0b1);
		else printf("%d", tmp&0b1);
	}
	printf("\n");
}

unsigned int packCharacters(unsigned int a, unsigned int b)
{
	unsigned int ret = a;
	ret <<= 8;
	ret += b;
	return ret;
}

int main(int argc, char const *argv[])
{
	char a, b , c, d;
	unsigned int pack = 0;

	scanf("%c %c %c %c", &a, &b, &c, &d);

	printf("%c:\n", a); displayBits(a);
	printf("%c:\n", b); displayBits(b);
	printf("%c:\n", c); displayBits(c);
	printf("%c:\n", d); displayBits(d);

	printf("\'%c\' and \'%c\' and \'%c\' and \'%c\' packed in an unsigned int:\n", a, b, c, d);
	pack = packCharacters(packCharacters(packCharacters(packCharacters(pack, a), b), c), d);
	displayBits(pack);

	return 0;
}
