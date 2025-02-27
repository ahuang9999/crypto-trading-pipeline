import pytest
from pysrc.main import buffer
import numpy as np


def test_buffer() -> None:
    ticks = [
        [(97381.02, 973.81, False)],
        [(97381.02, 973.81, False)],
        [(97381.02, 973.81, False)],
        [(97406.77, 10000.00, True)],
        [(97406.77, 12468.07, True)],
        [(97381.02, 973.8102, False)],
        [(97381.02, 973.8102, False)],
        [(97381.02, 973.8102, False)],
        [(97499.59, 10000.00, True)],
        [(97381.02, 973.8102, False)],
    ]
    targets = [
        0.001,
        -0.001,
        0.002,
        -0.002,
        0.0015,
        -0.0015,
        0.0005,
        -0.0005,
        -0.00077,
    ]
    assert len(ticks) - 1 == len(targets)
    next_midprice, model, predictions = buffer(ticks, targets, 97390.0)
    assert model is not None
    assert predictions is not None
    assert isinstance(model.coef_, np.ndarray)
    assert isinstance(model.intercept_, float)
    assert isinstance(next_midprice, float)
    assert next_midprice != 0
    assert isinstance(predictions, np.ndarray)
