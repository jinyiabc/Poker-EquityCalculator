


#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <cmath>
#include <iostream>
#include <omp/CardRange.h>
#include <omp/EquityCalculator.h>

std::string holeCardsToChar(const std::array<uint8_t,2>& holeCard) {
	std::string s;
    char tmp,tmp1;
    for( int i =0; i<2; i++){
        switch(holeCard[i]%13) {
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
        switch(holeCard[i]%4) {
            case 3: tmp1 = 's';
			        break;
            case 2: tmp1= 'h';
			        break;
            case 1: tmp1 = 'c';
			        break;
            case 0: tmp1 = 'd';
			        break;
        }
        s.push_back(tmp);
        s.push_back(tmp1);
    }
    return s;
}

const double& montecarlo(const std::vector<std::string>& ranges, std::string board, std::string dead)
{ 
    std::vector<omp::CardRange> ranges2(ranges.begin(), ranges.end());
    omp::EquityCalculator eq;
    eq.start(ranges2, omp::CardRange::getCardMask(board), omp::CardRange::getCardMask(dead), true);
    eq.wait();
    auto results = eq.getResults();

    // Returns a list of card combinations belonging to this range. Guarantees that there are no duplicates.
    // Cards in each combo are ordered so that the bigger rank is always first. The whole vector is sorted in the
    // following order: 1) rank of first card 2) rank of second card 3) suit of first card 4) suit of second card
    // Create a Hand from a card. CardIdx is an integer between 0 and 51, so that CARD = 4 * RANK + SUIT, where
    // rank ranges from 0 (deuce) to 12 (ace) and suit is from 0 (spade) to 3 (diamond).
    for (std::string const& c : ranges) {
        std::vector<std::array<uint8_t,2>> temp = omp::CardRange(c).combinations();
        size_t size1 = temp.size();
        for (int j=0; j < size1; j++){
//            std::cout << " " << temp[j][0] << temp[j][1];
            std::cout << " " << holeCardsToChar(temp[j]);
        }
        std::cout << size1 << std::endl;
    }
    std::cout << results.equity[0] << " " << results.equity[1] <<" "<< results.equity[2] << std::endl;
    std::cout << results.equity[3] << " " << results.equity[4] << " " << results.equity[5] << std::endl;

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

