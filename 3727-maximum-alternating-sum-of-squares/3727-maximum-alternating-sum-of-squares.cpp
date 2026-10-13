class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        sort(nums.begin(), nums.end(),
             [](int a, int b) {
                 return abs(a) < abs(b);
             });

        int n = nums.size();
        long long ans = 0;

        for (int i = 0; i < n / 2; i++) {
            long long x = abs(nums[i]);
            ans -= x * x;
        }

        for (int i = n / 2; i < n; i++) {
            long long x = abs(nums[i]);
            ans += x * x;
        }

        return ans;
    }
};