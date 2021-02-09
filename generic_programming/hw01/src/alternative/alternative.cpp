#include <bits/stdc++.h>

using namespace std;

struct  strtab_cmp
{
    typedef  vector<char>::iterator  strtab_iterator;

    bool  operator()( const pair<strtab_iterator, strtab_iterator>& x,
                       const pair<strtab_iterator, strtab_iterator>& y ) const {
        return lexicographical_compare( x.first, x.second, y.first, y.second );
    }
};

struct  strtab_print
{
    typedef  vector<char>::iterator strtab_iterator;
    ostream& out;

    strtab_print(ostream&  os) : out (os) {}

    void  operator()( const pair<strtab_iterator, strtab_iterator>&  s ) const {
        copy( s.first, s.second, ostream_iterator<char>(cout) );
    }
};


int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    
    freopen(argv[1], "r", stdin);
    ofstream out;
    string filename = "output/alternative_time.txt";
    out.open(filename, ios::out|ios::app);


    out << argv[2] << '-' << argv[3] << '\n';



    vector<char>  strtab;	   // Create string table
    char  c;
    clock_t t, head;



    t = head = clock();
    while (cin.get(c)) {
        strtab.push_back(c);
    }
    t = clock() - t;
    out << setw(20) << "Character Table:" << setw(15) << fixed << setprecision(8) << (long double)t/CLOCKS_PER_SEC << " seconds.\n";



    // Parse the string table into lines.
    typedef  vector<char>::iterator  strtab_iterator;
    vector<pair<strtab_iterator, strtab_iterator>> lines;
    strtab_iterator  start = strtab.begin();


    t = clock();
    while (start != strtab.end()) {
        strtab_iterator  next = find( start, strtab.end(), '\n' );

        if (next != strtab.end())
            ++next;
        lines.push_back( make_pair( start, next ) );
        start = next;
    }
    t = clock() - t;
    out << setw(20) << "Input:" << setw(15) << fixed << setprecision(8) << (long double)t/CLOCKS_PER_SEC << " seconds.\n";




    // Sort the vector of lines
    t = clock();
    sort( lines.begin(), lines.end(), strtab_cmp() );
    t = clock() - t;
    out << setw(20) << "Sorting:" << setw(15) << fixed << setprecision(8) << (long double)t/CLOCKS_PER_SEC << " seconds.\n";



    t = clock();
    // Write the lines to standard output
    for_each( lines.begin(), lines.end(), strtab_print(cout) );
    t = clock() - t;
    out << setw(20) << "Output:" << setw(15) << fixed << setprecision(8) << (long double)t/CLOCKS_PER_SEC << " seconds.\n";



    t = clock() - head;
    out << setw(20) << "Total:" << setw(15) << fixed << setprecision(8) << (long double)t/CLOCKS_PER_SEC << " seconds.\n\n\n\n";

    out.close();

    return 0;
}
