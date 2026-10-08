class Solution {
public:
    string removeOuterParentheses(string s) {
        string result;
        int balance = 0;

        for (char ch : s) {
            if (ch == '(') {
                // Outer opening bracket ko skip karo
                if (balance > 0)
                    result += ch;

                balance++;
            }
            else {
                balance--;

                // Outer closing bracket ko skip karo
                if (balance > 0)
                    result += ch;
            }
        }

        return result;
    }
};