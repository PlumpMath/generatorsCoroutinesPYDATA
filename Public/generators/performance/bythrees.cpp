#include <iostream>
#include <fstream>
#include <string>

using std::string;
using std::cin;
using std::cout;
using std::endl;

int main( int argc, char* argv[] ) {

	int i = 0;
	string bufs[3];
	cin >> bufs[0];
	cin >> bufs[1];
	cin >> bufs[2];
	while( !cin.fail() ) {
		cout << bufs[i] << ", " << bufs[(i+1)%3] << ", " << bufs[(i+2)%3] << endl;
		cin >> bufs[i];
		i = (i+1)%3;
	}

	return 0;
}
