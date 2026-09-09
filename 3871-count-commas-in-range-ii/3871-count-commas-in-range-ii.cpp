#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long countCommas(long long n) {
        long long ans = 0;

        // Numbers from 1,000 to 999,999 have 1 comma
        // Numbers from 1,000,000 to 999,999,999 have 2 commas
        // and so on.
        
        long long start = 1000;
        long long commas = 1;

        while (start <= n) {
            long long end;

            // Avoid overflow
            if (start > n / 1000)
                end = n;
            else
                end = min(n, start * 1000 - 1);

            ans += (end - start + 1) * commas;

            if (start > n / 1000)
                break;

            start *= 1000;
            commas++;
        }

        return ans;
    }
};