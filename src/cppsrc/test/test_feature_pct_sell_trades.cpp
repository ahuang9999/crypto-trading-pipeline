#include "../base_feature.hpp"
#include "gtest/gtest.h"
using namespace intproj;

TEST(FeatureTests, PctSellTest)
{
    PercentSellFeature psf;
    EXPECT_EQ(psf.compute_feature({ { 1, 1, false } }), 1);
    EXPECT_EQ(psf.compute_feature({ { 1, 1, false }, { 1, 1, true } }), 0.5);
    EXPECT_NEAR(psf.compute_feature({ { 1, 1, false }, { 1, 1, true }, { 1, 2, false } }), 0.67, 0.01);
}
