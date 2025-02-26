#include "base_feature.hpp"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <tuple>
#include <vector>

namespace intproj {

class FiveTickVolumeFeature : public BaseFeature
{
  public:
    float compute_feature(std::vector<std::tuple<float, float, bool>> data) override
    {
        int tickVolume = 0;
        for (auto t : data) { tickVolume += std::get<1>(t); }
        volumeInTicks.push_back(tickVolume);
        int volume = 0;
        if (volumeInTicks.size() <= 5) {
            for (int i : volumeInTicks) volume += i;
        } else {
            volumeInTicks.erase(volumeInTicks.begin());
            for (int i = 4; i >= 0; i--) { volume += volumeInTicks[i]; }
        }
        return static_cast<float>(volume);
    }

  private:
    std::vector<int> volumeInTicks;
};

}// namespace intproj