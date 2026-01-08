# hello_robot.py
# 作者: haha
# 日期: 2026-01-08
# 目的: 学习 Python 基础 + OpenArm 命令管理
# 功能: 输出信息、检查状态、记录日志

from datetime import datetime  # 用于获取当前时间


# ================= 函数区 =================

def check_arm_status(status):
    """
    检查机械臂状态并输出建议
    参数: status (str) - 机械臂当前状态
    """
    if status == "已复位":
        print("机械臂已复位，可以开始遥操作！")
        print("建议命令：./launch_dual_bilateral_with_aggregator.sh")
    elif status == "绑定中":
        print("CAN 正在绑定，请稍等...")
    else:
        print("请先复位机械臂！")
        print("复位命令：./reset_to_initial.sh both")


def log_operation(message):
    """
    记录操作日志到 robot_log.txt 文件
    参数: message (str) - 要记录的消息
    """
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{now}] {message}\n"
    
        with open("robot_log.txt", "a") as file:
            file.write(log_line)
    
        print(f"已记录日志：{log_line.strip()}")
    except Exception as e:
        print(f"日志记录失败：{e}")
        print("可能是权限或路径问题，继续运行...")

# ================= 主程序区 =================

def main():
    print("你好！我是 Python 程序")
    print("今天是 2026 年 1 月，我开始学 Python 了！")
    
    # 变量
    name = "haha"
    age = 20
    is_learning_git = True
    
    print(f"我的名字是：{name}")
    print(f"我今年 {age} 岁")
    print(f"我在学 Git 和 Python：{is_learning_git}")
    
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
    
    # 条件判断 + 函数调用
    arm_status = "已复位"  # 可以改成其他值测试
    print("\n当前机械臂状态检查：")
    check_arm_status(arm_status)
    
    # 日志记录
    print("\n记录日志：")
    log_operation("启动相机成功")
    log_operation("复位右臂完成")
    
    # 命令完整性检查
    required_commands = ["绑定 CAN", "启动相机", "复位双臂"]
    print("\n检查命令完整性：")
    for cmd in required_commands:
        if "复位" in cmd:
            print(f"{cmd} - 重要！必须先执行")
        else:
            print(f"{cmd} - OK")

    # ================= 新增：交互输入 =================
    print("\n=== 交互模式：请输入机械臂当前状态 ===")
    print("可选状态：已复位 / 绑定中 / 未复位 / 退出")
    print("输入 '退出' 结束程序")


    # ================= 新增：字典 - 命令数据库 =================
    # 字典（dict）：键是命令简称，值是元组（说明, 密码/参数）
    commands_db = {
        "绑定 CAN": ("绑定 CAN 口，需要密码", "123456"),
        "启动相机": ("启动所有相机话题", "./start_cameras.sh"),
        "复位双臂": ("复位左右臂到初始位", "./reset_to_initial.sh both"),
        "遥操作": ("启动双臂遥操作", "./launch_dual_bilateral_with_aggregator.sh"),
        "采集数据": ("启动数据采集并保存视频", "ros2 launch openarm_vla_collector   vla_collector_16d.launch.py save_videos:=true")
    }

    # 在 main() 里加：显示命令数据库
    print("\nOpenArm 命令数据库（字典）：")
    for cmd, (desc, param) in commands_db.items():
        print(f"- {cmd}: {desc}")
        if param:  # 如果有参数/密码
            print(f"  参数/密码: {param}")





    while True:  # 一直循环，直到用户输入“退出”
        user_input = input("请输入状态: ").strip()  # input() 获取用户键盘输入，strip() 去掉多余空格

        if user_input == "退出":
            print("程序退出，谢谢使用！")
            break  # 跳出循环，结束程序

    # 调用之前写的函数
        check_arm_status(user_input)

    # 记录用户操作到日志
        log_operation(f"用户输入状态：{user_input}")

# 程序入口（标准写法）
if __name__ == "__main__":
    main()
