from conan import ConanFile #type: ignore
from conan.tools.cmake import cmake_layout #type: ignore


class ExampleRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("gtest/1.15.0")
        self.requires("pybind11/2.13.6")
        self.requires("cpr/1.11.1")
        self.requires("nlohmann_json/3.11.3")


    def layout(self):
        cmake_layout(self)
