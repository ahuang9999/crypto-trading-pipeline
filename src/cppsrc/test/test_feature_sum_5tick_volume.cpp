#include "gtest/gtest.h"
#include "../base_feature.hpp"
using namespace intproj;

TEST(FeatureTests, TestSum5TickVolume)
{
    FiveTickVolumeFeature vf;
    EXPECT_EQ(vf.compute_feature({ { 2, 1, false } }), 1);
    EXPECT_EQ(vf.compute_feature({ { 1, 1, false } }), 2);
    EXPECT_EQ(vf.compute_feature({ { 1, 1, false }, { 1, 1, true } }), 4);
    EXPECT_EQ(vf.compute_feature({ { 1, 1, false }, { 1, 1, true } }), 6);
    EXPECT_EQ(vf.compute_feature({ { 2, 1, false }, { 1, 1, true } }), 8);
    EXPECT_EQ(vf.compute_feature({ { 1, 1, false }, { 1, 1, true } }), 9);
    EXPECT_EQ(vf.compute_feature({ { 2, 1, false }, { 1, 1, true } }), 10);
}
