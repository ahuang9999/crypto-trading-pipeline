import pytest
from pysrc import my_intern


def test_ntrades() -> None:
    NTrades_obj = my_intern.NTradesFeature()
    assert NTrades_obj.compute_feature([(1, 1, False)]) == 1
    assert NTrades_obj.compute_feature([(2, 1, False), (2, 2, True)]) == 2


def test_pctbuy() -> None:
    PctBuy_obj = my_intern.PercentBuyFeature()
    assert PctBuy_obj.compute_feature([(1, 1, False)]) == 0
    assert PctBuy_obj.compute_feature([(1, 1, False), (1, 1, True)]) == 0.5
    assert PctBuy_obj.compute_feature([(1, 1, True)]) == 1


def test_pctsell() -> None:
    PctSell_obj = my_intern.PercentSellFeature()
    assert PctSell_obj.compute_feature([(1, 1, False)]) == 1
    assert PctSell_obj.compute_feature([(1, 1, False), (1, 1, True)]) == 0.5
    assert PctSell_obj.compute_feature(
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
