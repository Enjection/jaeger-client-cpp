from conans import CMake
from conans import ConanFile


class JaegerClientCppConan(ConanFile):
    name = "jaeger-client-cpp"
    version = "0.0.6"
    description = ""
    author = "Innokentii Mokin <mia@tomsksoft.com>"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    build_requires = (
    )
    requires = (
        "thrift/0.11.0",
        "nlohmann_json/3.9.1",
        "yaml-cpp/0.6.3",
        "gtest/1.10.0",
        "opentracing-cpp/0.0.3",
        "libevent/2.1.12",
    )
    exports = "*"

    def configure(self):
        self.options["*"].shared = False
        self.options["*"].fPIC = True

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["JAEGERTRACING_BUILD_EXAMPLES"] = "OFF"
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["jaegertracing"]
