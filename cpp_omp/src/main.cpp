//#include <omp/EquityCalculator.h>
#include <iostream>
#include <pybind11/pybind11.h>
#include <omp/CardRange.h>
#include <string>
#include <iostream>
#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace py = pybind11;



//PYBIND11_MODULE(python_example, m) {
//	py::class_<omp::CardRange>(m, "CardRange")
//		.def(py::init<>())
//		.def(py::init<const std::string &>())
//		.def(py::init<const char*>())
//		.def(py::init<std::array<uint8_t, 2>>& > ());
//}


int main()
{
    //omp::EquityCalculator eq;
    //eq.start({"AK", "QQ"});
    //eq.wait();
    //auto r = eq.getResults();
    //std::cout << r.equity[0] << " " << r.equity[1] << std::endl;
	std::cout << std::string{ "AK" } << std::endl;
    omp::CardRange(std::string{ "AK" });
}
