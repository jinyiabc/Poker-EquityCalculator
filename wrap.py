import mc


def _run(ranges, cards_on_table, dead):
    equity = mc.montecarlo(ranges, cards_on_table, dead)
    print(equity)

    #  Constructs a range from an expression. Supported syntax:
    #  K4 : all suited and offsuited combos with specified ranks
    #  K4s : suited combos
    #  K4o : offsuited combos
    #  Kc4d : specific suits
    #  K4o+ : specified hand and all similar hands with a better kicker (K4 to KQ)
    #  44+ : pocket pair and all higher pairs
    #  K4+,Q8s,84 : multiple hands can be combined with comma
    #  random : all hands
    #  Spaces and non-matching characters in the end are ignored. The expressions are case-insensitive.


if __name__ == "__main__":
    ranges = ["K4o+", "AA", "33"]
    cards_on_table = "4hAd3c4c7c"
    dead = "6h"
    # _run(ranges, cards_on_table, dead)

    print(mc.playerCombos(ranges, cards_on_table, dead, 0))
    print(mc.playerCombos(ranges, cards_on_table, dead, 1))
    print(mc.playerCombos(ranges, cards_on_table, dead, 2))
    print(mc.playerCombos(ranges, cards_on_table, dead, 6))
    print(mc.playerCombos(["AK", "QsQd"], "4hAd3c4c7c", "", 1))