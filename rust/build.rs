extern crate prost_build;

macro_rules! vec_of_strings {
    ($($x:expr),*) => (vec![$($x.to_string()),*]);
}

use std::path::{PathBuf, Path};


fn main() -> std::io::Result<()> {
    let proto_files = vec_of_strings![
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
        "rtcm3.proto",
        "safety.proto",
        "sim_clock.proto",
        "status.proto",
        "timestamp.proto",
        "twist.proto",
        "vector3.proto",
        "wheel_odometry.proto"];
    let dir_proto = Path::new("proto");
    let dir_synapse_pb = Path::new("proto/synapse_pb");
    let mut files_abs: Vec<PathBuf> = Vec::new();
    for file in proto_files.iter() {
        let path = dir_synapse_pb.join(file);
        files_abs.push(path);
    };
    prost_build::compile_protos(&files_abs, &[dir_proto])?;
    Ok(())
}
