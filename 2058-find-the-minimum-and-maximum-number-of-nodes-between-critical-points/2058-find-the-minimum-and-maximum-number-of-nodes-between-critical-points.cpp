class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        vector<int> ans = {-1, -1};

        ListNode* prev = head;
        ListNode* curr = head->next;

        int index = 1;
        int first = -1;
        int last = -1;
        int minDist = INT_MAX;

        while (curr != nullptr && curr->next != nullptr) {
            // Check if curr is a local maximum or local minimum
            if ((curr->val > prev->val && curr->val > curr->next->val) ||
                (curr->val < prev->val && curr->val < curr->next->val)) {

                if (first == -1) {
                    // First critical point
                    first = index;
                } else {
                    // Distance from previous critical point
                    minDist = min(minDist, index - last);
                }

                last = index;
            }

            prev = curr;
            curr = curr->next;
            index++;
        }

        // Fewer than two critical points
        if (first == -1 || first == last)
            return ans;

        // Maximum distance is between first and last critical point
        int maxDist = last - first;

        return {minDist, maxDist};
    }
};