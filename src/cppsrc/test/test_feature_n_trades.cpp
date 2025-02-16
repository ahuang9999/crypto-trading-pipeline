#include "gtest/gtest.h"
#include "../base_feature.hpp"
using namespace intproj;

TEST(FeatureTests, NTradesTest)
{
    NTradesFeature ntf;
    EXPECT_EQ(ntf.compute_feature({{1, 1, false}}), 1);
    EXPECT_EQ(ntf.compute_feature({{2, 1, false}, {2, 2, true}}), 2);
}
