import pytest
from pysrc.main import buffer
from collections import deque

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
    targets: deque[float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert buffer(ticks, targets) is not None
