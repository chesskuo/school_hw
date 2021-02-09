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

	bool check = false;
	string str;

	while(getline(cin, str))
	{
		if(check) cout << '\n';

		smatch sm;
		vector<string> vs;

		while(regex_search(str, sm, regex("([A-Za-z]+)")))
		{
			vs.push_back(sm[0].str());
			str = sm.suffix().str();
		}

		sort(vs.begin(), vs.end(), greater<string>());
		for(auto i : vs)
			cout << i << '\n';

		check = true;
	}

	exit(0);
}
