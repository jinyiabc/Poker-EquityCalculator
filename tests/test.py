import mc
import pytest

def _runner(ranges, cards_on_table, dead, expected_result):
    equity = mc.montecarlo(ranges, cards_on_table, dead)
    assert equity == pytest.approx(expected_result, abs=1e-3)



def test_montecarlo1():
    """Three-way test"""
    ranges = ["K4o+", "AA", "33"]
    cards_on_table = "4hAd3c4c7c"
    dead = "6h"
    expected_results = [0.0, 1.0, 0.0]
    _runner(ranges, cards_on_table, dead, expected_results)

def test_montecarlo2():
    """Wrong Dead cards test """
    ranges = ["K4o+", "AA", "33"]
    cards_on_table = "4hAd3c4c7c"
    dead = "........."
    expected_results = [0.0, 1.0, 0.0]
    _runner(ranges, cards_on_table, dead, expected_results)

def test_montecarlo3():
    """blank board & dead test"""
    ranges = ["AK", "QQ"]
    cards_on_table = ""
    dead = ""
    expected_results = [0.439, 0.561]
    _runner(ranges, cards_on_table, dead, expected_results)

def test_montecarlo4():
    """random range test"""
    ranges = ["random", "AhTs"]
    cards_on_table = "7dJhKh4c"
    dead = ""
    expected_results = [0.504, 0.495]
    _runner(ranges, cards_on_table, dead, expected_results)


#assert mc.playerCombos(ranges, cards_on_table, dead, 0) == ['3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h']


