
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int p[150];
	int i, j;

	for(i=0; i<=100; i++) p[i] = 1;

	for(i=2; i<=100; i++)
		for(j=i*i; j<=100; j+=i)
			p[j] = 0;

	int cnt = 0;
	for(i=2; i<=100; i++)
	{
		if(p[i])
		{
			printf("%d ", i);
			cnt++;

			if(cnt%10 == 0) printf("\n");
		}
	}

	return 0;
}
