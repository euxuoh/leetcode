#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int sum = 0;
        int size = height.size();
        if (size < 3) {
            return sum;
        }
        
        vector<int> max_left(size);
        vector<int> max_right(size);

        for (int i = 1; i < height.size() - 1; ++i) {
            max_left[i] = max(max_left[i-1], height[i-1]);
        }

        for (int i = height.size() - 2; i >= 0; --i) {
            max_right[i] = max(max_right[i+1], height[i+1]);
        }

        for (int i = 1; i < height.size() - 1 ; ++i) {
            int m = min(max_left[i], max_right[i]);
            if (m > height[i]) {
                sum += (m - height[i]);
            }
        }

        return sum;
    }
};
