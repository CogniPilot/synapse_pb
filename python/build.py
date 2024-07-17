#!/usr/bin/env python3
import subprocess
from pathlib import Path

proto_files = [
    "actuators.proto",
    "altimeter.proto",
    "battery_state.proto",
    "bezier_curve.proto",
    "bezier_trajectory.proto",
    "bit32_flag.proto",
    "can.proto",
    "frame.proto",
    "header.proto",
    "imu.proto",
    "input.proto",
    "led_array.proto",
    "led.proto",
    "magnetic_field.proto",
    "nav_sat_fix.proto",
    "nav_sat_status.proto",
    "odometry.proto",
    "point.proto",
    "pose.proto",
    "pose_with_covariance.proto",
    "pwm.proto",
    "quaternion.proto",
    "safety.proto",
    "sim_clock.proto",
    "snap_setpoint.proto",
    "status.proto",
    "time.proto",
    "twist.proto",
    "twist_with_covariance.proto",
    "vector3.proto",
    "wheel_odometry.proto"];

dir_root = Path("../")
dir_python = Path(__file__).resolve().parent
dir_proto = dir_root / "proto"
dir_synapse_msgs = dir_proto / "synapse_pb"

proto_files_abs = [ dir_synapse_msgs / file for file in proto_files ]


subprocess.call(["protoc", "-I=" + str(dir_proto), "--python_out=" + str(dir_python)] + proto_files_abs)
