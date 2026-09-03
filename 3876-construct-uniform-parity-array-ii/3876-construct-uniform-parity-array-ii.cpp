class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        int mn = *min_element(nums1.begin(), nums1.end());

        // If the minimum element is odd,
        // every element can be made odd.
        if (mn % 2 == 1)
            return true;

        // If minimum is even, an odd element cannot be changed
        // because there is no smaller odd element for the first odd.
        for (int x : nums1) {
            if (x % 2 == 1)
                return false;
        }

        // All elements are even.
        return true;
    }
};