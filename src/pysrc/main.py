import argparse
import intern  # type: ignore
import time
from collections import deque
from sklearn import linear_model
from pysrc.data_client import DataClient
import numpy as np

if __name__ == "__main__":
    pass


def NTradesFeature(data: list[tuple[float, float, bool]]) -> float:
    obj = intern.NTradesFeature()
    compute: float = obj.compute_feature(data)
    return compute


def PercentBuyFeature(data: list[tuple[float, float, bool]]) -> float:
    obj = intern.PercentBuyFeature()
    compute: float = obj.compute_feature(data)
    return compute


def PercentSellFeature(data: list[tuple[float, float, bool]]) -> float:
    obj = intern.PercentSellFeature()
    compute: float = obj.compute_feature(data)
    return compute


def FiveTickVolumeFeature(data: list[tuple[float, float, bool]]) -> float:
    obj = intern.FiveTickVolumeFeature()
    compute: float = obj.compute_feature(data)
    return compute


def buffer(
    ticks: deque[list[tuple[float, float, bool]]], targets: deque[float]
) -> tuple[float, float]:
    X = []
    for trades in ticks:
        features = [
            NTradesFeature(trades),
            PercentBuyFeature(trades),
            PercentSellFeature(trades),
            FiveTickVolumeFeature(trades),
        ]
        X.append(features)
    # for row in X:
    #    for ele in row:
    #        print(ele,end=" ")
    #    print()

    clf = linear_model.Lasso(alpha=0.1)
    clf.fit(X, targets)
    return clf.coef_, clf.intercept_


def main() -> None:
    t = 1
    ticks: deque[list[tuple[float, float, bool]]] = deque(maxlen=10)
    targets: deque[float] = deque(maxlen=10)
    curMidprice: float = -5000.0

    obj = DataClient()

    while True:
        obj.__init__()
        print("Time = " + str(t) + "\n")

        trades_last_tick = obj.get_data(False)
        print((trades_last_tick["midprice"]))
        tupleList = []
        for data in trades_last_tick["buys"]:
            # data is pair of buys,amounts
            tempTuple = (data[0], round(data[0] * data[1], 2), True)
            tupleList.append(tempTuple)
        for data in trades_last_tick["sells"]:
            # data is pair of sells,amounts
            tempTuple = (data[0], round(data[0] * data[1], 2), False)
            tupleList.append(tempTuple)

        if not curMidprice == -5000.0:
            targets.append(trades_last_tick["midprice"] - curMidprice)
        curMidprice = trades_last_tick["midprice"]
        ticks.append(tupleList)

        t += 1
        time.sleep(1)
        if t <= 11:
            continue

        # else:
        # clf = linear_model.Lasso(alpha=0.5)
        # buffer(ticks,targets)


if __name__ == "__main__":
    main()
