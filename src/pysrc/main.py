import argparse
#import sys
#print("\n\n")
#print(sys.path)
#print("\n\n")
import intern # type: ignore 
import time
from collections import deque
from sklearn import linear_model
from pysrc.data_client import DataClient

if __name__ == "__main__":
    pass

def NTradesFeature(data):
    obj = intern.NTradesFeature()
    return obj.compute_feature(data)

def PercentBuyFeature(data):
    obj = intern.PercentBuyFeature()
    return obj.compute_feature(data)

def PercentSellFeature(data):
    obj = intern.PercentSellFeature()
    return obj.compute_feature(data)

def FiveTickVolumeFeature(data):
    obj = intern.FiveTickVolumeFeature()
    return obj.compute_feature(data)

def buffer(ticks,targets) -> tuple[float,float]:
    X = []
    for trades in ticks:
        features = [NTradesFeature(trades), PercentBuyFeature(trades),
                    PercentSellFeature(trades), FiveTickVolumeFeature(trades)]
        X.append(features)
    clf = linear_model.Lasso(alpha=0.1)
    clf.fit(X,targets)
    return clf.coef_, clf.intercept_

def main():
    t = 1
    ticks: deque[list[tuple[float,float,bool]]] = deque(maxlen=10)
    targets: deque[float] = deque(maxlen=10)
    curMidprice: float = -5000.0
    while True:
        print("Time = "+str(t)+"\n")
        obj = DataClient()
        trades_last_tick = obj.get_data(False)
        tupleList = []
        for data in trades_last_tick["buys"]:
            #data is pair of buys,amounts
            tempTuple = (data[0],round(data[0]*data[1],2),True)
            tupleList.append(tempTuple)
        for data in trades_last_tick["sells"]:
            #data is pair of sells,amounts
            tempTuple = (data[0],round(data[0]*data[1],2),False)
            tupleList.append(tempTuple)
        
        if (not curMidprice==-5000.0):
            targets.append(trades_last_tick["midprice"]-curMidprice)
        curMidprice = trades_last_tick["midprice"]
        ticks.append(tupleList)

        t+=1
        time.sleep(1)
        if t<=10:
            continue

        else:
            #clf = linear_model.Lasso(alpha=0.5)
            buffer(ticks,targets)



if __name__=="__main__":
    main()