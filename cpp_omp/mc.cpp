


#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <cmath>
#include <iostream>
#include <omp/CardRange.h>
#include <omp/EquityCalculator.h>

std::string holeCardsToChar(unsigned rank, unsigned suit) {
	std::string s;
    char tmp,tmp1;
    switch(rank) {
        case 12: tmp = 'A';
                break;
        case 11: tmp = 'K';
                break;
        case 10: tmp = 'Q';
                break;
        case 9: tmp = 'J';
                break;
        case 8: tmp = 'T';
                break;
        case 7: tmp = '9';
                break;
        case 6: tmp = '8';
                break;
        case 5: tmp = '7';
                break;
        case 4: tmp = '6';
                break;
        case 3: tmp = '5';
                break;
        case 2: tmp = '4';
                break;
        case 1: tmp = '3';
                break;
        case 0: tmp = '2';
                break;
    }
    switch(suit) {
        case 0: tmp1 = 's';
                break;
        case 1: tmp1= 'h';
                break;
        case 2: tmp1 = 'c';
                break;
        case 3: tmp1 = 'd';
                break;
    }
    s.push_back(tmp);
    s.push_back(tmp1);

    return s;
}

const double& montecarlo(const std::vector<std::string>& ranges, std::string board, std::string dead)
{ 
    std::vector<omp::CardRange> ranges2(ranges.begin(), ranges.end());
//    std::vector<omp::CardRange> ranges2;
//    for( std::string const & c : ranges ){
//        ranges2.push_back(omp::CardRange(c));
//    }
    omp::EquityCalculator eq;
    eq.start(ranges2, omp::CardRange::getCardMask(board), omp::CardRange::getCardMask(dead), true);
    eq.wait();
    auto results = eq.getResults();

    // Returns a list of card combinations belonging to this range. Guarantees that there are no duplicates.
    // Cards in each combo are ordered so that the bigger rank is always first. The whole vector is sorted in the
    // following order: 1) rank of first card 2) rank of second card 3) suit of first card 4) suit of second card
    // Create a Hand from a card. CardIdx is an integer between 0 and 51, so that CARD = 4 * RANK + SUIT, where
    // rank ranges from 0 (deuce) to 12 (ace) and suit is from 0 (spade) to 3 (diamond).
    std::cout << "----------- Original Range -----------" << std::endl;
    for (std::string const& c : ranges) {
        std::cout << c << std::endl;
        std::vector<std::array<uint8_t,2>> temp = omp::CardRange(c).combinations();
        size_t size1 = temp.size();
        for (int j=0; j < size1; j++){
            unsigned r1, r2, s1, s2;
            r1 = temp[j][0] >> 2 ;
            s1 = temp[j][0] &  3;
            r2 = temp[j][1] >> 2 ;
            s2 = temp[j][1] &  3;
            std::cout << " " << holeCardsToChar(r1, s1) << holeCardsToChar(r2, s2) ;
        }
        std::cout << std::endl;
        std::cout << "size of range: "<< size1 << std::endl;
    }

    // Set up card ranges.
    unsigned mCombinedRangeCount;
    uint64_t mDeadCards, mBoardCards;
    std::vector<omp::CardRange> mOriginalHandRanges;
    std::vector<std::vector<std::array<uint8_t,2>>> mHandRanges; // Ranges after card removal.
    static const size_t MAX_COMBINED_RANGE_SIZE = 10000;

    mDeadCards = omp::CardRange::getCardMask(dead);
    mBoardCards = omp::CardRange::getCardMask(board);
    mOriginalHandRanges = ranges2;
    mHandRanges = omp::EquityCalculator::removeInvalidCombos(ranges2, mDeadCards | mBoardCards);
    std::vector<omp::CombinedRange> combinedRanges = omp::CombinedRange::joinRanges(mHandRanges, MAX_COMBINED_RANGE_SIZE);
    for (unsigned i = 0; i < combinedRanges.size(); ++i) {
        if (combinedRanges[i].combos().size() == 0)
            return 0.0;
    }
    mCombinedRangeCount = (unsigned)combinedRanges.size();

    std::cout << "-----------Combined Range -----------" << std::endl;
    for(std::vector<std::array<uint8_t,2>> const& c : mHandRanges){
        size_t size2 = c.size();
        for( unsigned i=0; i<size2; i++){
            unsigned r1, r2, s1, s2;
            r1 = c[i][0] >> 2 ;
            s1 = c[i][0] &  3;
            r2 = c[i][1] >> 2 ;
            s2 = c[i][1] &  3;
            std::cout << " " << holeCardsToChar(r1, s1) << holeCardsToChar(r2, s2) ;
        }
        std::cout << std::endl;
        std::cout << "size of range: "<< size2 << std::endl;
    }
//    std::cout << results.equity[0] << " " << results.equity[1] <<" "<< results.equity[2] << std::endl;
//    std::cout << results.equity[3] << " " << results.equity[4] << " " << results.equity[5] << std::endl;

    std::array<double, 6> mydoubles{0, 0, 0, 0, 0, 0};
    for(int i = 0; i < ranges.size(); i++) {
        mydoubles[i] = i;
        std::cout << mydoubles[i] << std::endl;
    }

    return 10.0;

}




PYBIND11_MODULE(mc, m) {

    m.def("montecarlo", &montecarlo);
}

