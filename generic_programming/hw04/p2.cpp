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

		if(regex_match(str, sm, regex("([0-9]{4}\\-*){4}")))
		{
			cout << "TRUE" << ' ';

			int out = 0;

			for(int i=0; i<str.length(); i+=5)
			{
				string tmp = str.substr(i, 4);
				out += stoi(tmp);
				//cout << out;
			}
			cout << out << '\n';
			
		}
		else
		{
			cout << "FALSE" << '\n';
		}

		check = true;
	}

	exit(0);
}
