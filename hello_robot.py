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
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{now}] {message}\n"
    
    with open("robot_log.txt", "a") as file:
        file.write(log_line)
    
    print(f"已记录日志：{log_line.strip()}")


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


# 程序入口（标准写法）
if __name__ == "__main__":
    main()
