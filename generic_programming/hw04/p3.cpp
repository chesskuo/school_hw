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

	string str;

	while(getline(cin, str))
	{
		smatch sm;

		if(regex_search(str, sm, regex("\\+\\([0-9]{3}\\)\\-[0-9]-[0-9]{4}\\-[0-9]{4}")))
		{
			if(sm[0].str()[7] == sm[0].str()[9])
				cout << regex_replace(str, regex("\\([0-9]{3}\\)\\-[0-9]\\-[0-9]{4}"), "(XXX)-X-XXXX") << '\n';
			else
				cout << str << '\n';
		}
		else
			cout << str << '\n';
	}

	exit(0);
}
