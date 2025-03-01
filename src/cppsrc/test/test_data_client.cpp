#include "../data_client.hpp"
#include <gtest/gtest.h>

TEST(UnitTest, _parse_message)
{
    intproj::DataClient data = intproj::DataClient();

    nlohmann::json j1 = { { "timestamp", 1740687134 },
        { "timestampms", 1740687134118 },
        { "tid", 2840141254617266 },
        { "price", "83859.96" },
        { "amount", "0.23835984" },
        { "exchange", "gemini" },
        { "type", "sell" } };
    nlohmann::json j2 = { { "timestamp", 1740687133 },
        { "timestampms", 1740687133958 },
        { "tid", 2840141254617262 },
        { "price", "83906.7" },
        { "amount", "0.11917992" },
        { "exchange", "gemini" },
        { "type", "buy" } };
    nlohmann::json j3 = { { "timestamp", 1740687125 },
        { "timestampms", 1740687125373 },
        { "tid", 2840141254617166 },
        { "price", "83906.7" },
        { "amount", "0.002" },
        { "exchange", "gemini" },
        { "type", "buy" } };
    nlohmann::json message = { j1, j2, j3 };
    data._parse_message(message);
    ASSERT_NEAR(data.getMidprice(), 83883.33, 0.01);
    std::vector<std::tuple<float, float>> my_buys = { std::make_tuple(83906.7, 0.11917992),
        std::make_tuple(83906.7, 0.002) };
    std::vector<std::tuple<float, float>> my_sells = { std::make_tuple(83859.96, 0.23835984) };
    ASSERT_EQ(data.getBuys(), my_buys);
    ASSERT_EQ(data.getSells(), my_sells);
}


TEST(UnitTest, _get_data)
{
    intproj::DataClient data = intproj::DataClient();
    std::tuple result = data.get_data(false);
    ASSERT_FALSE(std::isnan(std::get<2>(result)));
}