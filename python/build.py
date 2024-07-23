#!/usr/bin/env python3
import subprocess
from pathlib import Path

proto_files = [
    "actuators.proto",
    "altimeter.proto",
    "battery_state.proto",
    "bezier_trajectory.proto",
    "clock_offset.proto",
    "covariance3.proto",
    "covariance6.proto",
    "duration.proto",
    "frame.proto",
    "imu.proto",
    "input.proto",
    "led_array.proto",
    "magnetic_field.proto",
    "nav_sat_fix.proto",
    "odometry.proto",
    "pose.proto",
    "pwm.proto",
    "quaternion.proto",
    "safety.proto",
    "sim_clock.proto",
    "status.proto",
    "timestamp.proto",
    "twist.proto",
    "uptime.proto",
    "vector3.proto",
    "vector3_array.proto",
    "wheel_odometry.proto"];

dir_root = Path("../")
dir_python = Path(__file__).resolve().parent
dir_proto = dir_root / "proto"
dir_synapse_msgs = dir_proto / "synapse_pb"

proto_files_abs = [ dir_synapse_msgs / file for file in proto_files ]


subprocess.call(["protoc", "-I=" + str(dir_proto), "--python_out=" + str(dir_python)] + proto_files_abs)
