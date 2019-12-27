#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	unsigned int num;
	int check[32] = {0};

	while(scanf("%d", &num) && num != -1)
	{
		check[num] = 1;
	}

	for(int i=0; i<32; i++) if(check[i] == 1) printf("%d ", i);
	printf("\n");

	int cas = 1;
	while(scanf("%u", &num) != EOF)
	{
		printf("Case %d: %u\n", cas++, num);

		int bin[32] = {0};
		int all = 1, exist = 0;

		for(int i=0; i<32; i++)
		{
			int tmp = num;
			tmp <<= i;
			tmp >>= 31;
			bin[i] = tmp & 0b1;
		}

		for(int i=0; i<32; i++)
		{
			if(check[i] == 1 && bin[31-i] == 0) all = 0;
			if(check[i] == 1 && bin[31-i] == 1) exist = 1;
		}

		if(all) printf("true");
		else printf("false");
		printf("(all bits 1)\n");

		if(exist) printf("true");
		else printf("false");
		printf("(exist bits 1)\n");
	}

	return 0;
}