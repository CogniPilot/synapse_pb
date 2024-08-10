set(PROTO_FILES
    synapse_pb/actuators.proto
    synapse_pb/altimeter.proto
    synapse_pb/battery_state.proto
    synapse_pb/bezier_trajectory.proto
    synapse_pb/clock_offset.proto
    synapse_pb/covariance3.proto
    synapse_pb/covariance6.proto
    synapse_pb/duration.proto
    synapse_pb/frame.proto
    synapse_pb/imu.proto
    synapse_pb/imu_q31_array.proto
    synapse_pb/input.proto
    synapse_pb/led_array.proto
    synapse_pb/magnetic_field.proto
    synapse_pb/nav_sat_fix.proto
    synapse_pb/odometry.proto
    synapse_pb/pose.proto
    synapse_pb/pwm.proto
    synapse_pb/quaternion.proto
    synapse_pb/safety.proto
    synapse_pb/sim_clock.proto
    synapse_pb/status.proto
    synapse_pb/timestamp.proto
    synapse_pb/twist.proto
    synapse_pb/uptime.proto
    synapse_pb/vector3.proto
    synapse_pb/wheel_odometry.proto
    )

set(PROTO_SRCS)
set(PROTO_HDRS)

set(IMPORT_DIRS "${CMAKE_CURRENT_SOURCE_DIR}")
message(STATUS "import dirs: ${IMPORT_DIRS}")

file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/synapse_pb)

protobuf_generate(
    PROTOC_OUT_DIR "${CMAKE_CURRENT_BINARY_DIR}"
    LANGUAGE cpp
    OUT_VAR outvar
    IMPORT_DIRS ${IMPORT_DIRS}
    PROTOS ${PROTO_FILES})

foreach(_file ${outvar})
    if (_file MATCHES "cc$")
        list(APPEND PROTO_SRCS ${_file})
    elseif (_file MATCHES "h$")
        list(APPEND PROTO_HDRS ${_file})
    elseif (_file MATCHES "hpp$")
        list(APPEND PROTO_HDRS ${_file})
    endif()
endforeach()

message(STATUS "proto_src: ${PROTO_SRCS}")
message(STATUS "proto_hdrs: ${PROTO_HDRS}")

add_library(${PROJECT_NAME}
  ${PROTO_SRCS}
  ${PROTO_HDRS}
)

ament_target_dependencies(${PROJECT_NAME} Protobuf) 

target_include_directories(${PROJECT_NAME}
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>
        $<INSTALL_INTERFACE:include>)

install(
    TARGETS ${PROJECT_NAME}
    EXPORT ${PROJECT_NAME}
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
)

install(FILES
    ${PROTO_HDRS}
    DESTINATION include/${PROJECT_NAME}
)

# vi: et ts=4 sw=4
