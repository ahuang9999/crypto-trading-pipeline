#pragma once

#include <math.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <tuple>
#include <vector>

namespace intproj {

class BaseFeature
{
  public:
    virtual float compute_feature(std::vector<std::tuple<float, float, bool>> data) = 0;

    virtual ~BaseFeature() {}
};

class PyBaseFeature : public BaseFeature
{
  public:
    using BaseFeature::BaseFeature;
    float compute_feature(std::vector<std::tuple<float, float, bool>> data) override
    {
        PYBIND11_OVERRIDE_PURE(float, BaseFeature, compute_feature, data);
    }
};


}// namespace intproj
