class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # dp[c] = number of distinct subsequences ending with character c
        dp = [0] * 26
        
        total = 0
        
        for ch in s:
            i = ord(ch) - ord('a')
            
            # New subsequences ending with ch
            new = (total + 1) % MOD
            
            # Remove old subsequences ending with the same character
            total = (total + new - dp[i]) % MOD
            
            dp[i] = new
        
        return total