cmake_minimum_required(VERSION 3.8)
project(carriage_drop_control)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(cv_bridge REQUIRED)

install(
  DIRECTORY carriage_drop_control
  DESTINATION lib/python3.10/site-packages
)

ament_package()
