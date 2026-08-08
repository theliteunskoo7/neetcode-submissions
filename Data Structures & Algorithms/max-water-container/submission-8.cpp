class Solution {
public:
    int maxArea(vector<int>& heights) {
        int op = 0;
        int n = heights.size();
        int i = 0;
        int j = n - 1;
        while (i < j) {
            int b = (j - i) * min(heights[j], heights[i]);
            op = max(op, b);
            if (heights[i] > heights[j]) {
                j--;
            } else {
                i++;
            }
        }
        return op;
    }
};