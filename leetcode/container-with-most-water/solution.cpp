class Solution {
public:

    int maxArea(vector<int>& height) {
        int best = 0;
        int l = 0;
        int r = height.size() - 1;
        while (l < r) {
            int area = (r - l)*(height[l] < height[r] ? height[l] : height[r]);
            best = (area > best? area : best);
            if (height[l] < height[r]) {
                ++l;
            } else {
                --r;
            }
        }
        return best;
    }
};
