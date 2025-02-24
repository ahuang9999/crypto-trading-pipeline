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

class NTradesFeature : public BaseFeature
{
  public:
    float compute_feature(std::vector<std::tuple<float, float, bool>> data) override
    {
        return (float)data.size();
    }
};

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
