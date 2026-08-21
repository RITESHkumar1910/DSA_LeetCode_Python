class Solution {
public:
    long long gcd(long long a, long long b) {
        while (b != 0) {
            long long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    long long lcm(long long a, long long b) {
        return a / gcd(a, b) * b;
    }

    long long findKthSmallest(vector<int>& coins, int k) {
        int n = coins.size();

        // Count how many distinct valid amounts are <= x
        auto count = [&](long long x) {
            long long ans = 0;

            // Inclusion-Exclusion
            for (int mask = 1; mask < (1 << n); mask++) {
                long long L = 1;
                int cnt = 0;
                bool tooLarge = false;

                for (int i = 0; i < n; i++) {
                    if (mask & (1 << i)) {
                        cnt++;

                        L = lcm(L, (long long)coins[i]);

                        if (L > x) {
                            tooLarge = true;
                            break;
                        }
                    }
                }

                if (tooLarge)
                    continue;

                long long ways = x / L;

                if (cnt % 2 == 1)
                    ans += ways;
                else
                    ans -= ways;
            }

            return ans;
        };

        long long low = 1;
        long long high = 1LL * (*min_element(coins.begin(), coins.end())) * k;

        while (low < high) {
            long long mid = low + (high - low) / 2;

            if (count(mid) >= k)
                high = mid;
            else
                low = mid + 1;
        }

        return low;
    }
};