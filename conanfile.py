from conans import ConanFile, CMake, tools
import os


class EstringConan(ConanFile):
    name = "estring"
    version = "1.2.3"
    license = "MIT"
    url = "https://github.com/sunxfancy/estring"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    requires = "libiconv/1.14.4@sunxfancy/stable", "libcharsetdetect/1.1.2@sunxfancy/stable", "gtest/1.8.0@lasote/stable"
    default_options = "shared=False", "gtest:shared=False"
    generators = "cmake"
    build_policy = "missing"
    exports_sources = "*"

    def build(self):
        cmake = CMake(self)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        cmake.configure(shared)
        cmake.build()

    def imports(self):
        self.copy(pattern="*.dll", dst="bin", src="bin")
        self.copy(pattern="*.so*", dst="bin", src="lib")
        self.copy(pattern="*.dylib", dst="bin", src="lib")

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.a", dst="lib", src="lib", keep_path=False)
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.dll", dst="bin", src="bin", keep_path=False)
        self.copy("*.dll", dst="bin", src="lib", keep_path=False)
        self.copy("*.so*", dst="lib", src="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["estring", "iconv", "charsetdetect"]
