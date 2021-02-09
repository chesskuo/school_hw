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

	string dna, goal, ori("ACGT");

	while(cin >> dna >> goal)
	{
		for(int i=0; i<dna.length(); i++)
			dna[i] = toupper(dna[i]);
		for(int i=0; i<goal.length(); i++)
			goal[i] = toupper(goal[i]);

		for(int i=0; i<4; i++)
			cout << count(dna.begin(), dna.end(), ori[i]) << (i==3 ? '\n' : ' ');

		int cnt = 0;
		string::iterator it = search(dna.begin(), dna.end(), goal.begin(), goal.end());

		while(it != dna.end())
		{
			cnt++;
			cout << it - dna.begin() << ' ';
			it++;
			it = search(it, dna.end(), goal.begin(), goal.end());
		}

		cout << cnt << '\n';
	}
	
	exit(0);
}
