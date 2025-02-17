import pytest
from pysrc import intern # type: ignore 
from pysrc.main import *


def test_pybind() -> None:
    assert intern.add(4, 5) == 9

def test_ntrades():
    assert NTradesFeature([(1,1,False)]) == 1
    assert NTradesFeature([(2,1,False), (2,2,True)]) == 2

def test_pctbuy():
    assert PercentBuyFeature([(1,1,False)]) == 0
    assert PercentBuyFeature([(1,1,False), (1,1,True)]) == 0.5
    assert PercentBuyFeature([(1,1,True)]) == 1

def test_pctsell():
    assert PercentSellFeature([(1,1,False)]) == 1
    assert PercentSellFeature([(1,1,False), (1,1,True)]) == 0.5
    assert PercentSellFeature([(1,1,False), (1,1,True), (1,2,False)]) == 0.67

def test_5tickvolume():
    assert FiveTickVolumeFeature([(2,1,False)]) == 1
    assert FiveTickVolumeFeature([(1,1,False)]) == 2
    assert FiveTickVolumeFeature([(1,1,False),(1,1,True)]) == 4
    assert FiveTickVolumeFeature([(1,1,False),(1,1,True)]) == 6
    assert FiveTickVolumeFeature([(2,1,False),(1,1,True)]) == 8
    assert FiveTickVolumeFeature([(1,1,False),(1,1,True)]) == 9
    assert FiveTickVolumeFeature([(2,1,False),(1,1,True)]) == 10