class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        int n = s.size();
        int m = n / 2;

        // Count characters
        vector<int> cnt(26, 0);

        for (char ch : s) {
            cnt[ch - 'a']++;
        }

        // Check if palindrome is possible
        int odd = 0;
        char middle = '\0';

        for (int i = 0; i < 26; i++) {
            if (cnt[i] % 2) {
                odd++;
                middle = char('a' + i);
            }
        }

        if (odd > 1)
            return "";

        // Characters available for the left half
        vector<int> half(26);

        for (int i = 0; i < 26; i++) {
            half[i] = cnt[i] / 2;
        }

        string targetHalf = target.substr(0, m);

        // --------------------------------------------------
        // Case 1: targetHalf itself can be formed
        // --------------------------------------------------
        vector<int> rem = half;
        bool possible = true;

        for (char ch : targetHalf) {
            int x = ch - 'a';

            if (rem[x] == 0) {
                possible = false;
                break;
            }

            rem[x]--;
        }

        // If exact target half is possible,
        // check the complete palindrome.
        if (possible) {
            string left = targetHalf;

            string mid = "";
            if (n % 2)
                mid += middle;

            string candidate = left + mid;

            string reverseLeft = left;
            reverse(reverseLeft.begin(), reverseLeft.end());

            candidate += reverseLeft;

            if (candidate > target)
                return candidate;
        }

        // --------------------------------------------------
        // Case 2: Make the left half just greater
        // than targetHalf
        // --------------------------------------------------

        for (int i = m - 1; i >= 0; i--) {

            // Characters available for targetHalf[0 ... i-1]
            rem = half;

            bool validPrefix = true;

            for (int j = 0; j < i; j++) {
                int x = targetHalf[j] - 'a';

                if (rem[x] == 0) {
                    validPrefix = false;
                    break;
                }

                rem[x]--;
            }

            if (!validPrefix)
                continue;

            // Try the smallest character greater than target[i]
            int current = targetHalf[i] - 'a';

            for (int c = current + 1; c < 26; c++) {

                if (rem[c] == 0)
                    continue;

                rem[c]--;

                // Build smallest possible suffix
                string suffix = "";

                for (int k = 0; k < 26; k++) {
                    suffix += string(rem[k], char('a' + k));
                }

                string left = targetHalf.substr(0, i);

                left += char('a' + c);
                left += suffix;

                // Build palindrome
                string mid = "";

                if (n % 2)
                    mid += middle;

                string reverseLeft = left;
                reverse(reverseLeft.begin(), reverseLeft.end());

                string answer = left + mid + reverseLeft;

                return answer;
            }
        }

        return "";
    }
};