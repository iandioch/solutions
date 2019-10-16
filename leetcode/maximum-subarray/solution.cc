class Solution {
public:
    
    inline int max(int a, int b) {
        return (a > b ? a : b);
    }

    int maxSubArray(vector<int>& nums) {
        int best = nums[0];
        int curr = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            curr = max(curr + nums[i], nums[i]);
            best = max(curr, best);
        }
        return best;
    }
};
