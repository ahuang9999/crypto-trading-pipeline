#include "gtest/gtest.h"
#include "../base_feature.hpp"
using namespace intproj;

TEST(FeatureTests, PctBuyTest)
{
    PercentBuyFeature ptf;
    EXPECT_EQ(ptf.compute_feature({{1, 1, false}}), 0);
    EXPECT_EQ(ptf.compute_feature({{1, 1, false}, {1, 1, true}}), 0.5);
    EXPECT_EQ(ptf.compute_feature({{1, 1, true}}), 1);
}
