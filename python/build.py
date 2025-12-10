#!/usr/bin/env python3
import subprocess
import shutil
from pathlib import Path
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Generate Python protobufs")
    parser.add_argument(
        "--out",
        type=str,
        default=None,
        help="Output directory for generated Python package (default: ./synapse_pb next to build.py)",
    )
    return parser.parse_args()

def main():
    args = parse_args()
    dir_python = Path(__file__).resolve().parent

    if args.out is not None:
        dir_out = Path(args.out)
    else:
        dir_out = dir_python

    dir_out.mkdir(parents=True, exist_ok=True)

    proto_files = [
        "actuators.proto",
        "altimeter.proto",
        "argus_measure_frame.proto",
        "argus_pixel.proto",
        "argus_results.proto",
        "argus_results_aux.proto",
        "argus_results_bin.proto",
        "argus_results_debug.proto",
        "battery_state.proto",
        "bezier_trajectory.proto",
        "clock_offset.proto",
        "covariance3.proto",
        "covariance6.proto",
        "duration.proto",
        "frame.proto",
        "imu.proto",
        "imu_q31_array.proto",
        "input.proto",
        "led_array.proto",
        "magnetic_field.proto",
        "nav_sat_fix.proto",
        "odometry.proto",
        "pixart_paa3905.proto",
        "pose.proto",
        "pwm.proto",
        "quaternion.proto",
        "safety.proto",
        "sim_clock.proto",
        "status.proto",
        "timestamp.proto",
        "twist.proto",
        "vector3.proto",
        "wheel_odometry.proto"];

    dir_python = Path(__file__).resolve().parent
    dir_root = dir_python.parent
    dir_python_module_dir = dir_python / "synapse_pb"

    if dir_python_module_dir.is_dir():
        shutil.rmtree(dir_python_module_dir)
    dir_python_module_dir.mkdir(parents=True, exist_ok=True)

    dir_proto = dir_root / "proto"
    dir_synapse_pb = dir_proto / "synapse_pb"

    proto_files_abs = [ dir_synapse_pb / file for file in proto_files ]

    print("proto:", dir_proto)
    print("proto files abs:", proto_files_abs)
    print("dir out:", dir_out)

    subprocess.call(["protoc", "-I=" + str(dir_proto), "--python_out=" + str(dir_out)] + proto_files_abs)

    module_file = dir_python / "synapse_pb" / "__init__.py"
    module_file.touch()


if __name__ == "__main__":
    print("hello")
    main()
