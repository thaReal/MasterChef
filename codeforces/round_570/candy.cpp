#include <bits/stdc++.h>
#define forn(i, n) for (int i = 0; i < int(n); i++)

using namespace std;


int main() {
	int q;
	scanf("%d", &q);
	
	forn(i, q) {
		int n;
		scanf("%d", &n);
		
		unordered_map<int, int> cbox;
		forn(j, n) {
			int x;
			scanf("%d", &x);
			
			// create a lookup table and get a count of each type of candy
			unordered_map<int, int>:: iterator it = cbox.find(x);
			if (it != cbox.end()) {
				it->second++;
			} else {
				cbox.insert(make_pair(x, 1));
			}
		}
		
		// create a vector(?) containing just values since the actual 
		// type of candy isn't important, just the number of each
		vector<int> candy;
		unordered_map<int, int>:: iterator itr;
		for (itr = cbox.begin(); itr != cbox.end(); itr++) {
			candy.push_back(itr->second);
		}
		
		// sort vector in descending order
		sort(candy.begin(), candy.end(), greater<int>());
		
		int mx = 0;
		vector<int> sol;
		for (auto k = candy.begin(); k != candy.end(); ++k) {
			if (k == candy.begin()) {
				sol.push_back(*k);
				mx = *k;
				
			} else if (mx == 0) {
				break;
				
			} else if (*k >= mx) {
				mx--;
				sol.push_back(mx);
			
			} else {
				sol.push_back(*k);
				mx = *k;
			}
		}
		cout << accumulate(sol.begin(), sol.end(), 0) << endl;
	}	
	
	return 0;
}
