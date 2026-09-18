#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> maxNumOfSubstrings(string s) {
        int n = s.length();
        vector<int> l(26, INT_MAX), r(26, -1);
        
        // Step 1: Find first and last positions of each character
        for (int i = 0; i < n; ++i) {
            int ch = s[i] - 'a';
            l[ch] = min(l[ch], i);
            r[ch] = max(r[ch], i);
        }

        vector<pair<int, int>> intervals;

        // Step 2: Expand intervals to satisfy condition 2
        for (int i = 0; i < 26; ++i) {
            if (l[i] == INT_MAX) continue;

            int left = l[i];
            int right = r[i];
            bool valid = true;

            for (int j = left; j <= right; ++j) {
                int ch = s[j] - 'a';
                if (l[ch] < left) {
                    // Valid substring must start at or after original first occurrence
                    valid = false;
                    break;
                }
                right = max(right, r[ch]);
            }

            if (valid) {
                intervals.push_back({right, left}); // Store end position first for easy sorting
            }
        }

        // Step 3: Sort intervals by end position
        sort(intervals.begin(), intervals.end());

        // Step 4: Greedy interval selection
        vector<string> result;
        int prev_end = -1;

        for (const auto& [right, left] : intervals) {
            if (left > prev_end) {
                result.push_back(s.substr(left, right - left + 1));
                prev_end = right;
            }
        }

        return result;
    }
};