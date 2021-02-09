#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	#ifdef DBG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif

	ios::sync_with_stdio(false);
	cin.tie(NULL);

	// ----------------------------------------

	int k;

	cin >> k;

	string str[k];

	for(int i=0; i<k; i++)
		cin >> str[i];

	int n;

	cin >> n;

	srand(time(NULL));

	for(int i=0; i<n; i++)
		cout << str[rand()%k] << (i==n-1?'\n':' ');
	
	exit(0);
}