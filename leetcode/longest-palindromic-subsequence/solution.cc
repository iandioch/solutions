#define max(a, b) ((a) > (b) ? (a) : (b))

class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.length();
        int dp[1001][1001];
        for (int i = n-1; i >= 0; --i) {
            dp[i][i] = 1;
            for (int j = i+1; j < n; ++j) {
                if (s[i] == s[j]) {
                    dp[i][j] = 2 + dp[i+1][j-1];
                } else {
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
                }
            }
        }
        return dp[0][n-1];
    }
};
