#include <gtest/gtest.h>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int func() {
    return 0;
}


TEST(MyTest, single) {
    EXPECT_EQ(func(), 4);
}

int main(int argc, char *argv[]) {
    testing::InitGoogleTest(&argc, argv);
    
    return RUN_ALL_TESTS();
}
