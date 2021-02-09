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

		if(regex_match(str, sm, regex("[0-9]*((\\.[0-9]*([Ee][\\+\\-]?[0-9]+)?[FfLl]?)|([Ee][0-9]+[FfLl]))")))
		{
			cout << "TRUE\n";
		}
		else
		{
			cout << "FALSE\n";

			vector<string> vs;

			while(regex_search(str, sm, regex("[[0-9]*((\\.[0-9]*([Ee][\\+\\-]?[0-9]+)?[FfLl]?)|([Ee][0-9]+[FfLl]))")))
			{
				vs.push_back(sm[0].str());
				str = sm.suffix().str();
			}

			for(auto i : vs)
				cout << i << '\n';
		}
		

		check = true;
	}

	exit(0);
}
