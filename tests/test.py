import mc
import pytest

def _runner(ranges, cards_on_table, dead, expected_result):
    equity = mc.montecarlo(ranges, cards_on_table, dead)
    assert equity == pytest.approx(expected_result, abs=1e-3)

def _runner1(ranges, cards_on_table, dead, playerID, expected_result):
    combos = mc.playerCombos(ranges, cards_on_table, dead, playerID)
    print(combos)
    assert len(combos) == pytest.approx(expected_result, abs=1e-3)

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

def test_playerCombos1():
    """random range test"""
    ranges = ["random", "AhTs"]
    cards_on_table = "7dJhKh4c"
    dead = ""
    playerID = 6
    expected_results = 1035
    _runner1(ranges, cards_on_table, dead, playerID, expected_results)

def test_playerCombos2():
    """Card removal test for preflop"""
    ranges = ["random", "AhTs"]
    cards_on_table = ""
    dead = ""
    playerID = 6
    expected_results = 1225   # C(50,2)
    _runner1(ranges, cards_on_table, dead, playerID, expected_results)

def test_playerCombos3():
    """Card removal test for flop"""
    ranges = ["random", "AhTs"]
    cards_on_table = "7dJhKh"
    dead = ""
    playerID = 6
    expected_results = 1081   # C(47,2)
    _runner1(ranges, cards_on_table, dead, playerID, expected_results)

def test_playerCombos4():
    """Customized range test for pair combos"""
    ranges = ["66+"]
    cards_on_table = ""
    dead = ""
    playerID = 6
    expected_results = 54   # 9*6 = 54
    _runner1(ranges, cards_on_table, dead, playerID, expected_results)

def test_playerCombos5():
    """Customized range test"""
    ranges = ["66+,AJs+,KJs+,QJs,AJo+,KJo+,QJo"]
    cards_on_table = ""
    dead = ""
    playerID = 6
    expected_results = 150
    _runner1(ranges, cards_on_table, dead, playerID, expected_results)

def test_playerCombos6():
    """Customized range test by dead card"""
    ranges = ["66+,AJs+,KJs+,QJs,AJo+,KJo+,QJo"]
    cards_on_table = ""
    dead = "AhTd"
    playerID = 6
    expected_results = 132
    _runner1(ranges, cards_on_table, dead, playerID, expected_results)

# 66+,AJs+,KJs+,QJs,AJo+,KJo+,QJo

#assert mc.playerCombos(ranges, cards_on_table, dead, 0) == ['3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3h3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3s', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h', '3d3h']


