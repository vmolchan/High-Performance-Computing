find_package(PythonInterp REQUIRED)

configure_file(${CMAKE_SOURCE_DIR}/test/test.py ${CMAKE_BINARY_DIR}/test/test.py COPYONLY)
add_test(NAME test COMMAND ${PYTHON_EXECUTABLE} "${CMAKE_CURRENT_BINARY_DIR}/test.py")
