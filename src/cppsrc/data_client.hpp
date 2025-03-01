#include <chrono>
#include <cmath>
#include <cpr/cpr.h>
#include <iostream>
#include <nlohmann/json.hpp>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>
#include <string>
#include <tuple>
#include <vector>

namespace intproj {

static int TIME_BETWEEN_TICKS = 30;

class DataClient
{
    std::vector<std::tuple<float, float>> buys;
    std::vector<std::tuple<float, float>> sells;
    float midprice = -2.0;

  public:
    DataClient() {}

    ~DataClient() {}

    void _query_api(bool sandbox)
    {
        auto now = std::chrono::system_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::seconds>(now.time_since_epoch());
        int seconds = duration.count();
        std::string url;
        if (sandbox) {
            url = "https://api.sandbox.gemini.com/v1/trades/btcusd?since_tid=0&limit_trades=3";
        } else {
            url = "https://api.gemini.com/v1/trades/btcusd/?timestamp=" + std::to_string(seconds - TIME_BETWEEN_TICKS);
        }
        cpr::Response response = cpr::Get(cpr::Url{ url }, cpr::VerifySsl{ false });
        try {
            nlohmann::json json_response = nlohmann::json::parse(response.text);
            _parse_message(json_response);
        } catch (...) {
            std::cerr << "Error, could not fetch json" << std::endl;
        }
    }

    void _parse_message(const nlohmann::json &message)
    {
        float lowestAsk = 1000000.0;
        float highestBid = 0.0;
        for (auto &x : message) {
            float price = std::stof(x["price"].get<std::string>());
            float amount = std::stof(x["amount"].get<std::string>());
            if (x["type"] == "buy") {
                if (price < lowestAsk) lowestAsk = price;
                this->buys.push_back(std::make_tuple(price, amount));
            } else {
                if (price > highestBid) highestBid = price;
                this->sells.push_back(std::make_tuple(price, amount));
            }
        }
        if (lowestAsk == 1000000.0 || highestBid == 0.0) {
            this->midprice = -2;
        } else {
            this->midprice = std::ceil((lowestAsk + highestBid) / 2.0 * 100.0) / 100.0;
        }
    }

    std::tuple<std::vector<std::tuple<float, float>>, std::vector<std::tuple<float, float>>, float> get_data(
      bool sandbox)
    {
        buys.clear();
        sells.clear();
        _query_api(sandbox);
        return std::make_tuple(this->buys, this->sells, this->midprice);
    }

    float getMidprice()
    {
        return this->midprice;
    }
    std::vector<std::tuple<float, float>> getBuys()
    {
        return this->buys;
    }
    std::vector<std::tuple<float, float>> getSells()
    {
        return this->sells;
    }
};


}// namespace intproj