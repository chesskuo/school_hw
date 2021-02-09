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

	int n;
	string str;
	vector<string> vs;
	multiset<string> ms;

	cin >> n;

	for(int i=0; i<n; i++)
	{
		cin >> str;
		ms.insert(str);
	}

	int times;
	
	cin >> times;

	for(int i=0; i<times; i++)
		vs.push_back(str);
	
	for(auto i : vs)
	{
		multiset<string>::iterator it;
		
		it = find(ms.begin(), ms.end(), i);

		if(it != ms.end())
			cout << "Yes, we have " << count(ms.begin(), ms.end(), i) << " " << i << ".\n";
		else
			cout << "No, We don't have this animal.\n";
	}
	
	exit(0);
}
