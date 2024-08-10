# SPDX-License-Identifier: Apache-2.0
if (CONFIG_SYNAPSE_PB)

list(APPEND CMAKE_MODULE_PATH ${ZEPHYR_BASE}/modules/nanopb)
include(nanopb)

set(SYNAPSE_PB_DIR ${ZEPHYR_CURRENT_MODULE_DIR})
set(PROTO_DIR ${SYNAPSE_PB_DIR}/proto/synapse_pb)
 
file(GLOB OPTION_FILES "${PROTO_DIR}/*.option")
   
set(NANOPB_IMPORT_DIRS "${SYNAPSE_PB_DIR}/proto")
set(NANOPB_OPTIONS "-I${CMAKE_SOURCE_DIR}/proto")

zephyr_library_named(synapse_pb)

# sorted in dependency order
set(PROTO_FILES
    ${PROTO_DIR}/actuators.proto
    ${PROTO_DIR}/altimeter.proto
    ${PROTO_DIR}/battery_state.proto
    ${PROTO_DIR}/bezier_trajectory.proto
    ${PROTO_DIR}/clock_offset.proto
    ${PROTO_DIR}/covariance3.proto
    ${PROTO_DIR}/covariance6.proto
    ${PROTO_DIR}/duration.proto
    ${PROTO_DIR}/frame.proto
    ${PROTO_DIR}/imu.proto
    ${PROTO_DIR}/imu_q31_array.proto
    ${PROTO_DIR}/input.proto
    ${PROTO_DIR}/led_array.proto
    ${PROTO_DIR}/magnetic_field.proto
    ${PROTO_DIR}/nav_sat_fix.proto
    ${PROTO_DIR}/odometry.proto
    ${PROTO_DIR}/pose.proto
    ${PROTO_DIR}/pwm.proto
    ${PROTO_DIR}/quaternion.proto
    ${PROTO_DIR}/safety.proto
    ${PROTO_DIR}/sim_clock.proto
    ${PROTO_DIR}/status.proto
    ${PROTO_DIR}/timestamp.proto
    ${PROTO_DIR}/twist.proto
    ${PROTO_DIR}/uptime.proto
    ${PROTO_DIR}/vector3.proto
    ${PROTO_DIR}/wheel_odometry.proto
    )

foreach(FILE ${PROTO_FILES})
  zephyr_nanopb_sources(synapse_pb ${FILE})
endforeach()

# we need to be able to include generated header files
zephyr_library_include_directories(
  ${CMAKE_CURRENT_BINARY_DIR}/..
)

zephyr_include_directories(
  ${CMAKE_CURRENT_BINARY_DIR}/..
)

# necessary for module to calll nanopb_generate
add_dependencies(app synapse_pb)

endif()
