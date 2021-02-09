#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    
    freopen(argv[1], "r", stdin);
    ofstream out;
    string filename = "output/simple_time.txt";
    out.open(filename, ios::out|ios::app);

    vector<string> V;      // Container
    string tmp;



    out << argv[2] << '-' << argv[3] << '\n';


    

    clock_t t, head;

    t = head = clock();
    while ( getline(cin, tmp) )
         V.push_back(tmp);
    t = clock() - t;
    out << setw(20) << "Input:" << setw(15) << fixed << setprecision(8) << (long double)t/CLOCKS_PER_SEC << " seconds.\n";



    t = clock();
    sort( V.begin(), V.end() );
    t = clock() - t;
    out << setw(20) << "Sorting:" << setw(15) << fixed << setprecision(8) << (long double)t/CLOCKS_PER_SEC << " seconds.\n";



    t = clock();
    copy( V.begin(), V.end(), ostream_iterator<string>(cout, "\n") );
    t = clock() - t;
    out << setw(20) << "Output:" << setw(15) << fixed << setprecision(8) << (long double)t/CLOCKS_PER_SEC << " seconds.\n";



    t = clock() - head;
    out << setw(20) << "Total:" << setw(15) << fixed << setprecision(8) << (long double)t/CLOCKS_PER_SEC << " seconds.\n\n\n\n";



    out.close();

    return 0;
}