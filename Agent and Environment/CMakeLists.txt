cmake_minimum_required(VERSION 3.24)
project(testcpp)

set(CMAKE_CXX_STANDARD 17)

add_executable(Agent_and_Environment main.cpp Agent.cpp Agent.h Environment.cpp Environment.h Direction.h)
