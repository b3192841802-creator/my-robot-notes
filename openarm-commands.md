# OpenArm 常用命令笔记

## 启动流程
1. 绑定 CAN: ./auto_bind_can.sh (密码: 123456)
2. 启动相机: ./start_cameras.sh
3. 启动遥操: ./launch_dual_bilateral_with_aggregator.sh

## 复位
- 单臂: ./reset_to_initial.sh left/right
- 双臂: ./reset_to_initial.sh both

## 数据采集
ros2 launch openarm_vla_collector vla_collector_16d.launch.py save_videos:=true
