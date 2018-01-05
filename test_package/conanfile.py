from conans import ConanFile, CMake
import os

# This easily allows to copy the package in other user or channel
channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "sunxfancy")

class HelloReuseConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "estring/1.2.2@%s/%s" % (username, channel)
    generators = "cmake"
    build_policy = "missing"

    def build(self):
        cmake = CMake(self)
        print('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        # equal to ./bin/greet, but portable win: .\bin\greet
        self.run(os.sep.join([".","bin", "libtest"]))

    def imports(self):
        self.copy(pattern="*.dll", dst="bin", src="bin")
        self.copy(pattern="*.so*", dst="bin", src="lib")
        self.copy(pattern="*.dylib", dst="bin", src="lib")
