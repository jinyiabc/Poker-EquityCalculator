CombinedRange(unsigned playerIdx, const std::vector<std::array<uint8_t,2>>& holeCards);

    // Set up card ranges.
    mDeadCards = deadCards;
    mBoardCards = boardCards;
    mOriginalHandRanges = handRanges;
    mHandRanges = removeInvalidCombos(handRanges, mDeadCards | mBoardCards);
    std::vector<CombinedRange> combinedRanges = CombinedRange::joinRanges(mHandRanges, MAX_COMBINED_RANGE_SIZE);
    for (unsigned i = 0; i < combinedRanges.size(); ++i) {
        if (combinedRanges[i].combos().size() == 0)
            return false;
        if (!enumerateAll)
            combinedRanges[i].shuffle();
        mCombinedRanges[i] = combinedRanges[i];
    }
    mCombinedRangeCount = (unsigned)combinedRanges.size();


std::array<std::array<uint8_t,2>,MAX_PLAYERS> holeCards = combinedRange.combos()[comboIdx].holeCards;
const CombinedRange::Combo& combo = mCombinedRanges[i].combos()[comboIdx].holeCards;

    struct Combo
    {
        uint64_t cardMask;
        std::array<std::array<uint8_t,2>,MAX_PLAYERS> holeCards;
        Hand evalHands[MAX_PLAYERS];
    };