import argparse
from pysrc import my_intern  # type: ignore
import time

from sklearn import linear_model  # type: ignore
from sklearn.linear_model import Lasso  # type: ignore
from pysrc.data_client import DataClient
import numpy as np

if __name__ == "__main__":
    pass


TIME_BETWEEN_TICKS: int = 30


def write_to_file(filename: str, data: float) -> None:
    with open(filename, "a") as file:
        file.write("\n" + str(data))


def call_cpp_api(sandbox: bool) -> tuple:
    my_data_client = my_intern.DataClient()
    ret: tuple = my_data_client.get_data(sandbox)
    return ret


FiveTick_obj = my_intern.FiveTickVolumeFeature()


def NTradesFeature(data: list[tuple[float, float, bool]]) -> float:
    NTrades_obj = my_intern.NTradesFeature()
    compute: float = NTrades_obj.compute_feature(data)
    return compute


def PercentBuyFeature(data: list[tuple[float, float, bool]]) -> float:
    PctBuy_obj = my_intern.PercentBuyFeature()
    compute: float = PctBuy_obj.compute_feature(data)
    return compute


def PercentSellFeature(data: list[tuple[float, float, bool]]) -> float:
    PctSell_obj = my_intern.PercentSellFeature()
    compute: float = PctSell_obj.compute_feature(data)
    return compute


def FiveTickVolumeFeature(data: list[tuple[float, float, bool]]) -> float:
    compute: float = FiveTick_obj.compute_feature(data)
    return compute


def buffer(
    ticks: list[list[tuple[float, float, bool]]], targets: list[float], midprice: float
) -> tuple[float, Lasso, np.ndarray]:
    X = []
    for i in range(0, len(ticks) - 1):
        features = [
            NTradesFeature(ticks[i]),
            PercentBuyFeature(ticks[i]),
            PercentSellFeature(ticks[i]),
            FiveTickVolumeFeature(ticks[i]),
        ]
        X.append(features)
    X_test = np.array(
        [
            NTradesFeature(ticks[-1]),
            PercentBuyFeature(ticks[-1]),
            PercentSellFeature(ticks[-1]),
            FiveTickVolumeFeature(ticks[-1]),
        ]
    ).reshape(1, -1)

    clf = linear_model.Lasso(alpha=1)
    clf.fit(X, targets)
    predictions = clf.predict(X_test)
    next_midprice = midprice * (1 + predictions[0])
    return (round(next_midprice, 2), clf, predictions)


def main() -> None:
    f = open("src/pysrc/predictions.txt", "w")
    f.close()
    z = open("src/pysrc/targets.txt", "w")
    z.close()

    t = 1
    ticks: list[list[tuple[float, float, bool]]] = []
    targets: list[float] = []
    curMidprice: float = -5000.0
    predictedMidprice: float = 2

    while True:
        trades_last_tick = call_cpp_api(False)
        if trades_last_tick[2] == -2:
            time.sleep(TIME_BETWEEN_TICKS)
            continue

        print("\nTime = " + str(t) + "")
        if predictedMidprice != 2:
            print("Predicted midprice: " + str(round(predictedMidprice, 2)))
            write_to_file(
                "src/pysrc/targets.txt",
                (trades_last_tick[2] - curMidprice) / curMidprice,
            )
            write_to_file(
                "src/pysrc/predictions.txt", predictedMidprice / curMidprice - 1
            )

        print("Actual midprice: " + str(round(trades_last_tick[2], 2)))
        tupleList: list[tuple[float, float, bool]] = []
        for data in trades_last_tick[0]:
            # data is pair of buys,amounts
            tempTuple = (data[0], round(data[0] * data[1], 2), True)
            tupleList.append(tempTuple)
        for data in trades_last_tick[1]:
            # data is pair of sells,amounts
            tempTuple = (data[0], round(data[0] * data[1], 2), False)
            tupleList.append(tempTuple)

        if not curMidprice == -5000.0:
            targets.append((trades_last_tick[2] - curMidprice) / curMidprice)
        ticks.insert(len(ticks), tupleList)
        curMidprice = trades_last_tick[2]
        t += 1
        time.sleep(TIME_BETWEEN_TICKS)

        if t < 11:
            pass
        else:
            predictedMidprice = buffer(ticks, targets, curMidprice)[0]

            ticks.pop(0)
            targets.pop(0)


if __name__ == "__main__":
    main()
