#include <pybind11/pybind11.h>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace py = pybind11;

class Pet {
public:
    Pet(const std::string &name) : name(name) { }
    void setName(const std::string &name_) { name = name_; }
    const std::string &getName() const { return name; }
private:
    std::string name;
};

PYBIND11_MODULE(python_example, m) {
    py::class_<Pet>(m, "Pet", py::dynamic_attr())
        .def(py::init<const std::string &>())
        .def_property("name", &Pet::getName, &Pet::setName)
        .def("setName", &Pet::setName)
        .def("getName", &Pet::getName);
}
