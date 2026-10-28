cmake_minimum_required(VERSION 3.20)

project(OpenCVProject LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED COMPONENTS core highgui)

add_executable(OpenCVProject
    src/main.cpp
)

target_link_libraries(OpenCVProject
    PRIVATE ${OpenCV_LIBS}
)

target_include_directories(OpenCVProject
    PRIVATE ${OpenCV_INCLUDE_DIRS}
)
