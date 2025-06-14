#include "data_client.hpp"
#include "fivetick_feature.hpp"
#include "ntrades_feature.hpp"
#include "pctbuy_feature.hpp"
#include "pctsell_feature.hpp"
#include <iostream>
#include <pybind11/chrono.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>

using namespace intproj;
namespace py = pybind11;

int main()
{
    std::cout << "hello\n";
}

int add(int a, int b)
{
    return a + b;
}

float call_compute_feature(BaseFeature *feat)
{
    return feat->compute_feature({});
}

PYBIND11_MODULE(my_intern, m)
{
    m.doc() = "Feature computation";
    m.def("call_compute_feature", &call_compute_feature);
    py::class_<BaseFeature, PyBaseFeature /* <--- trampoline*/>(m, "BaseFeature")
      .def(py::init<>())
      .def("compute_feature", &BaseFeature::compute_feature);

    py::class_<NTradesFeature, BaseFeature>(m, "NTradesFeature").def(py::init<>());
    py::class_<PercentBuyFeature, BaseFeature>(m, "PercentBuyFeature").def(py::init<>());
    py::class_<PercentSellFeature, BaseFeature>(m, "PercentSellFeature").def(py::init<>());
    py::class_<FiveTickVolumeFeature, BaseFeature>(m, "FiveTickVolumeFeature").def(py::init<>());
    py::class_<DataClient>(m, "DataClient")
      .def(py::init<>())
      .def("get_data", &intproj::DataClient::get_data, py::arg("sandbox"));
}