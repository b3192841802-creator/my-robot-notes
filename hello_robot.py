# hello_robot.py
# 这是我的第一个 Python 程序
# 注释用 # 开头，不会执行

print("你好！我是 Python 程序")
print("今天是 2026 年 1 月，我开始学 Python 了！")

# 变量：不需要提前声明类型
name = "haha"
age = 20
is_learning_git = True

print("我的名字是：" + name)
print("我今年 " + str(age) + " 岁")          # 把数字转成字符串才能拼接
print(f"我在学 Git 和 Python：{is_learning_git}")   # f-string（最推荐的格式化方式）

# 列表 + 循环
commands = [
    "绑定 CAN: ./auto_bind_can.sh",
    "启动相机: ./start_cameras.sh",
    "复位双臂: ./reset_to_initial.sh both",
    "数据采集: ros2 launch ... vla_collector_16d.launch.py"
]

print("\nOpenArm 常用命令列表：")
for i, cmd in enumerate(commands, 1):
    print(f"{i}. {cmd}")


# 条件判断：if / elif / else
arm_status = "已复位"   # 可以改成 "已复位" 测试不同情况

if arm_status == "已复位":
    print("机械臂已复位，可以开始遥操作！")
    print("启动命令：./launch_dual_bilateral_with_aggregator.sh")
elif arm_status == "绑定中":
    print("CAN 正在绑定，请稍等...")
else:
    print("请先复位机械臂！")
    print("复位命令：./reset_to_initial.sh both")
