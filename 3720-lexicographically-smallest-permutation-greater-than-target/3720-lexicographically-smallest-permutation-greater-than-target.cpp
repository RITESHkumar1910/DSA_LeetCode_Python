class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = s.size();

        vector<int> cnt(26, 0);
        for (char c : s) {
            cnt[c - 'a']++;
        }

        // cntBefore[i] = character counts available before position i
        vector<vector<int>> cntBefore(n, vector<int>(26));

        int fail = n;

        // Match target from left to right
        for (int i = 0; i < n; i++) {
            cntBefore[i] = cnt;

            int x = target[i] - 'a';

            if (cnt[x] == 0) {
                fail = i;
                break;
            }

            cnt[x]--;
        }

        // Start from the rightmost possible position
        int start = (fail == n) ? n - 1 : fail;

        for (int i = start; i >= 0; i--) {

            vector<int> temp = cntBefore[i];

            int x = target[i] - 'a';

            // Find the smallest character greater than target[i]
            for (int y = x + 1; y < 26; y++) {

                if (temp[y] > 0) {
                    temp[y]--;

                    string ans = target.substr(0, i);
                    ans += char('a' + y);

                    // Add remaining characters in sorted order
                    for (int c = 0; c < 26; c++) {
                        ans += string(temp[c], char('a' + c));
                    }

                    return ans;
                }
            }
        }

        return "";
    }
};