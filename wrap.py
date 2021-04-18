import mc


def _run(ranges, cards_on_table, dead):
    equity = mc.montecarlo(ranges, cards_on_table, dead)
    print(equity)


if __name__ == "__main__":
    ranges = ["random", "AA", "33"]
    cards_on_table = "4hAd3c4c7c"
    dead = "6h"
    _run(ranges, cards_on_table, dead)
