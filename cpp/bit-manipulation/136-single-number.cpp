#include <gtest/gtest.h>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int singleNumber(vector<int>& nums) {
    if (nums.size() == 1) {
        return nums[0];
    }

    map<int, int> counter;
    int res;
    for (auto i = 0; i < nums.size(); ++i) {
        if (counter.count(nums[i])) {
            counter[nums[i]] += 1;
        } else {
            counter[nums[i]] = 1;
        }
    }
    for (auto v : counter) {
        cout << v.first << " " << v.second << endl;
        if (v.second == 1) {
            res = v.first;
            break;
        }
    }
    return res;
}

int singleNumber2(vector<int>& nums) {
    int res = 0;
    for (auto num: nums) {
        res ^= num;
    }
    return res;
}

TEST(MyTest, single) {
    vector<int> nums = {4, 2, 1, 2, 1};
    EXPECT_EQ(singleNumber(nums), 4);
}

int main(int argc, char *argv[]) {
    testing::InitGoogleTest(&argc, argv);
    
    return RUN_ALL_TESTS();
}
