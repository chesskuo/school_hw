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

	int page, words;
	string books, tmp;

	cin >> page >> words >> books;

	int p, w, n;

	while(cin >> p >> w >> n)
	{
		char now = books[(p - 1) * words + (w - 1)];
		int cnt = count(books.begin(), books.end(), now); // count this num

		cout << now << ' ' << cnt << ' ' << cnt%n << '\n';

		tmp += books[(p - 1) * words + (w - 1)];
	}

	cout << tmp << ' ';

	int cnt = 0;
	string::iterator it = books.begin();
	
	for(int i=0; i<page*words-tmp.length()+1; i++)
	{
		if(is_permutation(tmp.begin(), tmp.end(), it))
			cnt++;
		it++;
	}
	cout << cnt << '\n';

	exit(0);
}
