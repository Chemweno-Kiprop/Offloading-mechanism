from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        #  Camera node (replace with your camera driver)
        Node(
            package='usb_cam',  # or 'v4l2_camera' / your specific camera package
            executable='usb_cam_node_exe',
            name='camera',
            output='screen',
            parameters=[{
                'video_device': '/dev/video0',
                'frame_id': 'camera_frame',
                'image_width': 640,
                'image_height': 480,
                'framerate': 30.0
            }]
        ),

        #  Vision node (detect object and drop zone)
        Node(
            package='carriage_drop_control',
            executable='vision_node',
            name='vision_node',
            output='screen'
        ),

        # Drop control logic node
        Node(
            package='carriage_drop_control',
            executable='drop_control_node',
            name='drop_control_node',
            output='screen'
        ),

        #  Arduino bridge for servo
        Node(
            package='rosserial_python',
            executable='serial_node.py',
            name='ros_arduino_bridge',
            output='screen',
            arguments=['/dev/ttyACM0'],  # <-- change if your Arduino port differs
        ),
    ])
