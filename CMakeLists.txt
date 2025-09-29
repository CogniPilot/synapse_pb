cmake_minimum_required(VERSION 3.8)
project(synapse_pb)

find_package(ament_cmake REQUIRED)
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
find_package(Protobuf REQUIRED)

# Where to place the generated Python package in the build tree
set(SYNAPSE_PY_OUT "${CMAKE_CURRENT_BINARY_DIR}/gen/python")

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

add_subdirectory(proto)

file(MAKE_DIRECTORY ${SYNAPSE_PY_OUT})

# Generate the Python package using your script
add_custom_command(
  OUTPUT "${SYNAPSE_PY_OUT}/synapse_pb/__init__.py"
  COMMAND ${Python3_EXECUTABLE} "${CMAKE_CURRENT_SOURCE_DIR}/python/build.py" --out "${SYNAPSE_PY_OUT}"
  DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/python/build.py"
  WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/python"
  COMMENT "Generating synapse_pb Python package with build.py"
  VERBATIM
)

add_custom_target(synapse_pb_py ALL
  DEPENDS "${SYNAPSE_PY_OUT}/synapse_pb/__init__.py")

# Install the generated package into the workspace's site-packages
set(PY_INSTALL_DIR "lib/python${Python3_VERSION_MAJOR}.${Python3_VERSION_MINOR}/site-packages")
install(DIRECTORY "${SYNAPSE_PY_OUT}/synapse_pb/"
        DESTINATION "${PY_INSTALL_DIR}/synapse_pb")

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  #set(ament_cmake_copyright_FOUND TRUE)
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_export_targets(${PROJECT_NAME} HAS_LIBRARY_TARGET)
ament_export_dependencies(Protobuf)

ament_package()
