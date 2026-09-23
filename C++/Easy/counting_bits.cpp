#include <bits/stdc++.h>
#include <numeric>
using namespace std;

vector<int> count(int n) {
    
    vector<int> list;

    for (int i = 0; i <= n; i++) {
        int x = i;
        int s = 0;

        while (x > 0) {
            int rest = x % 2;
            s += rest;
            x /= 2;
        }

        list.push_back(s);
    }

    return list;
}