cmake_minimum_required(VERSION 3.20)

project(JebediahFirstborn LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED COMPONENTS core highgui imgproc videoio tracking)

add_executable(jebediah-firstborn src/main.cpp)

target_link_libraries(jebediah-firstborn PRIVATE ${OpenCV_LIBS})

target_include_directories(jebediah-firstborn PRIVATE ${OpenCV_INCLUDE_DIRS})
