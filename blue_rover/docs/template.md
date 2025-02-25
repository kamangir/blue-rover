# UGV Beast PI ROS2

- Order at: https://www.waveshare.com/ugv-beast-ros2-kit.htm

## Battery installation:

- instructions: https://www.youtube.com/watch?v=t3EXdMzEUrA

> ... 3 x 18650 lithium batteries with a capacity of 2200mA or above ~~and a discharge rate of 4C~~ (vape stores have them)

## Connection

Two modes:

1. AP (Access Point): provides a hotspot: `AccessPopup`, password: `1234567890`
2. STA (Station Mode): connects to a WiFi network.

- controller: http://<ip-address>:5000/ ("main program")
- Jupyter Lab: http://<ip-address>:8888/

## Disable the controller

for ROS or notebook access.

https://www.waveshare.com/wiki/UGV_Beast_PI_ROS2_1._Preparation#1.2_Disable_the_main_program_from_running_automatically

# SSH

```bash
ssh root@<ip-address> -p 23
```

password: `ws`

# ROS

🔥

- https://www.waveshare.com/wiki/UGV_Beast_PI_ROS2 🔥
- https://github.com/waveshareteam/ugv_rpi

