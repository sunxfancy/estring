﻿cmake_minimum_required(VERSION 2.8)
project("estring")

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/build/conanbuildinfo.cmake)
    include(${CMAKE_CURRENT_SOURCE_DIR}/build/conanbuildinfo.cmake)
else()
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
endif()
conan_basic_setup()

SET(VERSION_MAJOR "1")
SET(VERSION_MINOR "2")
SET(VERSION_PATCH "3")

SET (CMAKE_BUILD_TYPE Debug) # 默认构建Debug模式

include_directories(src include)

set( CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin )
set( CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib )
set( CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib )

file(GLOB_RECURSE source_files
        ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp
    )

# 生成动态库目标
add_library(${PROJECT_NAME} ${source_files})

# 链接动态库
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

# 指定动态库版本
# VERSION 动态库版本
# SOVERSION API版本
if (BUILD_SHARED_LIBS)
set_target_properties(${PROJECT_NAME} PROPERTIES VERSION ${VERSION_MAJOR}.${VERSION_MINOR}.${VERSION_PATCH} SOVERSION ${VERSION_MAJOR})
endif()

add_subdirectory(doc)
# add_subdirectory(test)
