#include "base_feature.hpp"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <tuple>
#include <vector>

namespace intproj {

class PercentBuyFeature : public BaseFeature
{
  public:
    float compute_feature(std::vector<std::tuple<float, float, bool>> data) override
    {
        float total = (float)data.size();
        int buy = 0;
        for (auto t : data) {
            if (std::get<2>(t)) buy++;
        }
        return buy / total;
    }
};

}// namespace intproj