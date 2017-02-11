project(LibTest)
cmake_minimum_required(VERSION 3.1)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set( CMAKE_CXX_STANDARD 98)
add_executable(test main.cpp)
target_link_libraries(test ${CONAN_LIBS})
