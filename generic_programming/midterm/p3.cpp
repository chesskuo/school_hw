#include <bits/stdc++.h>

using namespace std;

struct Stu
{
	string name;
	int english;
	int math;

	friend bool operator>(const Stu& l, const Stu& r)
	{
		int tmp = l.english + l.math;
		int tmpr = r.english + r.math;

		if(tmp == tmpr)
			return l.name > r.name;
		else
			return tmp > tmpr;
	}

	friend bool operator<(const Stu& l, const Stu& r)
	{
		int tmp = l.english + l.math;
		int tmpr = r.english + r.math;

		if(tmp == tmpr)
			return l.name < r.name;
		else
			return tmp < tmpr;
	}

	friend istream& operator>>(istream& in, Stu& r)
	{
		in >> r.name >> r.english >> r.math;
		return in;
	}

	friend ostream& operator<<(ostream& out, Stu& r)
	{
		out << r.name << ' ' << r.english << ' ' << r.math << '\n';
		return out;
	}
};

enum Way
{
	LESS,
	GREAT
};

template<Way way>
class RuntimeCmp : std::binary_function<Stu, Stu, bool>
{
public:
	bool operator()(const Stu& ls, const Stu& rs)
	{
		if(way == LESS)
			return ls < rs;
		else if(way == GREAT)
			return ls > rs;
	}
};

int main(int argc, char const *argv[])
{
	#ifdef DBG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif

	ios::sync_with_stdio(false);
	cin.tie(NULL);

	// ----------------------------------------

	int quan;
	Stu student;
	set<Stu, RuntimeCmp<LESS>> less;
	set<Stu, RuntimeCmp<GREAT>> great;

	cin >> quan;

	for(int i=0; i<quan; i++)
	{
		cin >> student;
		less.insert(student);
		great.insert(student);
	}

	cout << "Set A:\n";
	for(auto i : less)
		cout << i;

	cout << "\nSet B:\n";
	for(auto i : great)
		cout << i;

	exit(0);
}
