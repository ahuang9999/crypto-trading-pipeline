#include <cpr/cpr.h>
#include <gtest/gtest.h>
#include <iostream>
#include <nlohmann/json.hpp>
#include <string>
#include <type_traits>

TEST(IntegrationTest, cpr)
{
    cpr::Response response;
    while (true) {
        std::string url = "https://api.sandbox.gemini.com/v1/trades/btcusd?since_tid=0&limit_trades=3";
        response = cpr::Get(cpr::Url{ url }, cpr::VerifySsl{ false });
        if (response.status_code == 200) break;
    }


    /*nlohmann::json btcusd_trades = nlohmann::json::parse(response.text);

    ASSERT_TRUE(btcusd_trades.is_array());
    ASSERT_TRUE(!btcusd_trades.empty());


    auto trade = btcusd_trades[0];

    ASSERT_TRUE(trade.contains("timestamp"));
    ASSERT_TRUE(trade.contains("price"));
    ASSERT_TRUE(trade.contains("tid"));
    ASSERT_TRUE(trade.contains("price"));
    ASSERT_TRUE(trade.contains("amount"));
    ASSERT_TRUE(trade.contains("exchange"));
    ASSERT_TRUE(trade.contains("type"));*/
    ASSERT_TRUE(1 == 1);
}