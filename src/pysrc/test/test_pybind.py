import pytest
from pysrc import my_intern
from pysrc.main import (
    NTradesFeature,
    PercentBuyFeature,
    PercentSellFeature,
    FiveTickVolumeFeature,
)


def test_ntrades() -> None:
    assert NTradesFeature([(1, 1, False)]) == 1
    assert NTradesFeature([(2, 1, False), (2, 2, True)]) == 2


def test_pctbuy() -> None:
    assert PercentBuyFeature([(1, 1, False)]) == 0
    assert PercentBuyFeature([(1, 1, False), (1, 1, True)]) == 0.5
    assert PercentBuyFeature([(1, 1, True)]) == 1


def test_pctsell() -> None:
    assert PercentSellFeature([(1, 1, False)]) == 1
    assert PercentSellFeature([(1, 1, False), (1, 1, True)]) == 0.5
    assert PercentSellFeature(
        [(1, 1, False), (1, 1, True), (1, 2, False)]
    ) == pytest.approx(0.67, rel=1e-2)


def test_5tickvolume() -> None:
    FiveTick_obj = my_intern.FiveTickVolumeFeature()
    assert FiveTick_obj.compute_feature([(2, 1, False)]) == 1
    assert FiveTick_obj.compute_feature([(1, 1, False)]) == 2
    assert FiveTick_obj.compute_feature([(1, 1, False), (1, 1, True)]) == 4
    assert FiveTick_obj.compute_feature([(1, 1, False), (1, 1, True)]) == 6
    assert FiveTick_obj.compute_feature([(2, 1, False), (1, 1, True)]) == 8
    assert FiveTick_obj.compute_feature([(1, 1, False), (1, 1, True)]) == 9
    assert FiveTick_obj.compute_feature([(2, 1, False), (1, 1, True)]) == 10
