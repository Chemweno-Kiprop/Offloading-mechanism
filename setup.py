from setuptools import setup

package_name = 'carriage_drop_control'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='Vision and servo control for carriage drop system',
    license='MIT',
    entry_points={
        'console_scripts': [
            'vision_node = carriage_drop_control.vision_node:main',
            'drop_control_node = carriage_drop_control.drop_control_node:main',
        ],
    },
)
