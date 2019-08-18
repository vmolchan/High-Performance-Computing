find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_PATH})

find_package(NumPy REQUIRED)
include_directories(${PYTHON_NUMPY_INCLUDE_DIR})

find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})

###############################
### Add CMake commands here ###
###############################

add_library(iterate STATIC iterate.c)
target_include_directories(iterate PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

swig_add_library(iterate LANGUAGE python SOURCES iterate.i)
swig_link_libraries(iterate iterate)


###############################
###                         ###
###############################

configure_file(${CMAKE_SOURCE_DIR}/src/laplace.py ${CMAKE_BINARY_DIR}/src/laplace.py COPYONLY)
