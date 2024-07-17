extern crate prost_build;

macro_rules! vec_of_strings {
    ($($x:expr),*) => (vec![$($x.to_string()),*]);
}

use std::path::{PathBuf, Path};


fn main() -> std::io::Result<()> {
    let proto_files = vec_of_strings![
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
    let dir_proto = Path::new("../proto");
    let dir_synapse_pb = Path::new("../proto/synapse_pb");
    let mut files_abs: Vec<PathBuf> = Vec::new();
    for file in proto_files.iter() {
        let path = dir_synapse_pb.join(file);
        files_abs.push(path);
    };
    prost_build::compile_protos(&files_abs, &[dir_proto])?;
    Ok(())
}
