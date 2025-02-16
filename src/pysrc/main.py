import argparse
#import sys
#print("\n\n")
#print(sys.path)
#print("\n\n")
import intern
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

def main():
    t = 1
    ticks = []
    prices = []
    return1s = []
    while True:
        
        obj = DataClient()
        trades_last_tick = obj.get_data(False)
        temp = []
        for i in range(len(trades_last_tick["prices"])-1):
            tempTuple = (trades_last_tick["prices"][0],trades_last_tick["amounts"][0],trades_last_tick["types"][0])
            temp.append(tempTuple)
            
        ticks.append(temp)
        prices.append(trades_last_tick["prices"][0])
        if (len(prices)>=2):
            return1s.append( (prices[len(prices)-1]-prices[len(prices)-2])/prices[len(prices)-2] )
        if t<=10:
            continue

        else:
            #clf = linear_model.Lasso(alpha=0.5)
            t+=1
            X = []
            for trades in ticks:
                features = [NTradesFeature(trades), PercentBuyFeature(trades),
                            PercentSellFeature(trades), FiveTickVolumeFeature(trades)]
                X.append(features)
            clf = linear_model.Lasso(alpha=0.1)
            clf.fit(X,prices)


        t+=1