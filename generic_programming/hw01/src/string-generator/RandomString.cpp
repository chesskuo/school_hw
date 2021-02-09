#include <bits/stdc++.h>

using namespace std;

int n, m;
vector<string> vs;

char base[] = {
	'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
};

void random_string()
{
	srand(time(NULL));

	for(int i=0; i<n; i++)
	{
		string tmp;
		int len = m;

		for(int j=0; j<len; j++)
		{
			int index = rand() % 62;
			char buf[2];
			buf[0] = base[index];
			tmp += string(buf);
		}

		vs.push_back(tmp);
	}
}
int main(int argc, char const *argv[])
{
	vs.clear();

	n = atoi(argv[1]);
	m = atoi(argv[2]);

	string filename = "src/random_string.in";

	random_string();

	ofstream out;

	out.open(filename, ios::out|ios::trunc);

	for(auto i : vs)
		out << i << '\n';

	out.close();

	return 0;
}
