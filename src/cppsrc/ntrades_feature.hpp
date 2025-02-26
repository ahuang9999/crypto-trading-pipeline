#include "base_feature.hpp"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <tuple>
#include <vector>

namespace intproj {

class NTradesFeature : public BaseFeature
{
  public:
    float compute_feature(std::vector<std::tuple<float, float, bool>> data) override
    {
        return (float)data.size();
    }
};

}// namespace intproj