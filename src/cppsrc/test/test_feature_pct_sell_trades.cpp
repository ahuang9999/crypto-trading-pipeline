#include "gtest/gtest.h"
#include "../base_feature.hpp"
using namespace intproj;

TEST(FeatureTests, PctSellTest)
{
    PercentSellFeature psf;
    EXPECT_EQ(psf.compute_feature({{1, 1, false}}), 1);
    EXPECT_EQ(psf.compute_feature({{1, 1, false}, {1, 1, true}}), 0.5);
    EXPECT_EQ(psf.compute_feature({{1, 1, false}, {1, 1, true}, {1, 2, false}}), 0.67);
}
