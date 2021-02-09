#include <bits/stdc++.h>

#define TIME

using namespace std;

class line_iterator
{
	istream*  in;
	string   line;
	bool     at_end;

	void read() {
		if (*in)
			getline(*in, line);
		at_end = (*in) ? true : false;
	}

public:
	typedef  input_iterator_tag  iterator_category;
	typedef  string  value_type;
	typedef  ptrdiff_t  difference_type;
	typedef  const string*  pointer;
	typedef  const string&  reference;

	line_iterator(){
		in = &cin;
		at_end = false;
	}
	line_iterator(istream& s){
		in = &s;
		read();
	}
	reference operator*() const { return line; }
	pointer operator->() const { return &line; }

	line_iterator operator++() {  // prefix ++
		read();
		return *this;
	}

	line_iterator operator++(int) {  // postfix ++
		line_iterator  tmp = *this;
		read();
		return tmp;
	}

	bool operator==(const line_iterator& i) const {
		return (in == i.in && at_end == i.at_end) ||
			   (at_end == false && i.at_end == false);
	}

	bool operator!=(const line_iterator& i) const {
		return !(*this == i);
	}
}; // end  of class line_iterator

int  main(int argc, char const *argv[])
{
	ios::sync_with_stdio(false);
	
	freopen(argv[1], "r", stdin);
	ofstream out;
	string filename = "output/iterator_time.txt";
	out.open(filename, ios::out|ios::app);


	out << argv[2] << '-' << argv[3] << '\n';


	clock_t t, head;
	t = head = clock();

	line_iterator  iter(cin);
	line_iterator  end_of_file;

	vector<string>  V(iter, end_of_file);

	t = clock() - t;
	out << setw(20) << "Input:" << setw(15) << fixed << setprecision(8) << (long double)t/CLOCKS_PER_SEC << " seconds.\n";



	t = clock();
	sort( V.begin(), V.end() ); 
	t = clock() - t;
	out << setw(20) << "Sorting:" << setw(15) << fixed << setprecision(8) << (long double)t/CLOCKS_PER_SEC << " seconds.\n";


	t = clock();
	copy( V.begin(), V.end(), ostream_iterator<string>(cout, "\n"));
	t = clock() - t;
	out << setw(20) << "Output:" << setw(15) << fixed << setprecision(8) << (long double)t/CLOCKS_PER_SEC << " seconds.\n";



	t = clock() - head;
	out << setw(20) << "Total:" << setw(15) << fixed << setprecision(8) << (long double)t/CLOCKS_PER_SEC << " seconds.\n\n\n\n";




	out.close();

	return 0;
}
