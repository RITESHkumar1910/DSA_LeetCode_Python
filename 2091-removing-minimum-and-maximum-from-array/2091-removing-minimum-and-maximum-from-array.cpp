class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int n = nums.size();

        int minPos = 0, maxPos = 0;

        // Find positions of minimum and maximum
        for (int i = 1; i < n; i++) {
            if (nums[i] < nums[minPos])
                minPos = i;

            if (nums[i] > nums[maxPos])
                maxPos = i;
        }

        int left = min(minPos, maxPos);
        int right = max(minPos, maxPos);

        // 1. Remove both from the front
        int front = right + 1;

        // 2. Remove both from the back
        int back = n - left;

        // 3. Remove one from front and one from back
        int both = (left + 1) + (n - right);

        return min({front, back, both});
    }
};