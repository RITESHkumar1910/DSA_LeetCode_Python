class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        vector<int> pos;

      
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '1')
                pos.push_back(i);
        }

      
        if (pos.size() < k)
            return "";

        int minLen = INT_MAX;
        string ans = "";

      
        for (int i = 0; i + k - 1 < pos.size(); i++) {
            int l = pos[i];
            int r = pos[i + k - 1];

            int len = r - l + 1;

            string cur = s.substr(l, len);

            if (len < minLen) {
                minLen = len;
                ans = cur;
            }
            else if (len == minLen && cur < ans) {
                ans = cur;
            }
        }

        return ans;
    }
};