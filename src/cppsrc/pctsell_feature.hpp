#include "base_feature.hpp"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <tuple>
#include <vector>

namespace intproj {

class PercentSellFeature : public BaseFeature
{
  public:
    float compute_feature(std::vector<std::tuple<float, float, bool>> data) override
    {
        float total = (float)data.size();
        int sell = 0;
        for (auto t : data) {
            if (!(std::get<2>(t))) sell++;
        }
        return sell / total;
    }
};

}// namespace intproj