#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	char hex[] = "0123456789ABCDEF";
	unsigned int num;
	char num_h[8];
	int cas = 1;

	while(scanf("%u", &num) != EOF)
	{
		printf("Case %d: %u\n", cas++, num);

		for(int i=0; i<8; i++) num_h[i] = '0';
		
		int now = 1;
		do{
			num_h[8-(now++)] = hex[num&0xF];
			num >>= 4;
		} while(num > 0);

		for(int i=0; i<8; i++) printf("%c ", num_h[i]);
		printf("\n");
	}

	return 0;
}