#include <bits/stdc++.h>
#define forn(i, n) for (int i = 0; i < int(n); i++)

using namespace std;


int main() {
	int q;
	scanf("%d", &q);
	
	forn(i, q) {
		int n;
		scanf("%d", &n);
		
		unordered_map<int, int> candy;
		forn(j, n) {
			int x;
			scanf("%d", &x);
			
			unordered_map<int, int>:: iterator it = candy.find(x);
			if (it != candy.end()) {
				it->second++;
			} else {
				candy.insert(make_pair(x, 1));
			}
		}
		
		// debug code to print out unordered map
		unordered_map<int, int>:: iterator itr;
		for (itr = candy.begin(); itr != candy.end(); itr++) {
			cout << itr->first << " " << itr->second << endl;
		}
	}	
	
	return 0;
}
