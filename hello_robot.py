# hello_robot.py
# 作者: haha
# 日期: 2026-01-08
# 目的: 学习 Python 基础 + OpenArm 命令管理
# 功能: 输出信息、检查状态、记录日志

from datetime import datetime  # 用于获取当前时间
import sys

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



def print_help():
    print("\n用法：")
    print("  python3 hello_robot.py check [状态]          # 检查机械臂状态")
    print("  python3 hello_robot.py log [消息]            # 记录日志")
    print("  python3 hello_robot.py help                  # 显示帮助")
    print("\n示例：")
    print("  python3 hello_robot.py check 已复位")
    print("  python3 hello_robot.py log '相机启动成功'")



# ================= 主程序区 =================

def main():
    print("欢迎使用 OpenArm 辅助工具 v1.0")
    
    # ================= 命令行参数处理（新功能） =================
    if len(sys.argv) > 1:  # 如果有参数
        command = sys.argv[1].lower()  # 取第一个参数作为命令
        
        if command == "check" and len(sys.argv) >= 3:
            status = " ".join(sys.argv[2:])  # 支持带空格的状态，如 "已复位"
            print(f"快速检查状态：{status}")
            check_arm_status(status)
            log_operation(f"快速检查状态: {status}")
            return  # 执行完就退出，不走下面的交互
        
        elif command == "log" and len(sys.argv) >= 3:
            msg = " ".join(sys.argv[2:])
            log_operation(msg)
            return
        
        elif command == "help":
            print_help()
            return
        
        else:
            print("未知命令或参数不足")
            print_help()
            return
    
    # ================= 如果没有命令行参数，走原来的完整流程 =================
    # 变量输出（保留你原来的）
    name = "haha"
    age = 20
    is_learning_git = True
    
    print(f"我的名字是：{name}")
    print(f"我今年 {age} 岁")
    print(f"我在学 Git 和 Python：{is_learning_git}")
    
    # 列表 + 循环（保留）
    commands = [
        "绑定 CAN: ./auto_bind_can.sh",
        "启动相机: ./start_cameras.sh",
        "复位双臂: ./reset_to_initial.sh both",
        "数据采集: ros2 launch ... vla_collector_16d.launch.py"
    ]
    
    print("\nOpenArm 常用命令列表：")
    for i, cmd in enumerate(commands, 1):
        print(f"{i}. {cmd}")
    
    # 命令完整性检查（保留）
    required_commands = ["绑定 CAN", "启动相机", "复位双臂"]
    print("\n检查命令完整性：")
    for cmd in required_commands:
        if "复位" in cmd:
            print(f"{cmd} - 重要！必须先执行")
        else:
            print(f"{cmd} - OK")
    
    # 交互模式（保留）
    print("\n=== 交互模式：请输入机械臂当前状态 ===")
    print("可选状态：已复位 / 绑定中 / 未复位 / 退出")
    print("输入 '退出' 结束程序")
    
    while True:
        user_input = input("请输入状态: ").strip()
        if user_input == "退出":
            print("程序退出，谢谢使用！")
            break
        check_arm_status(user_input)
        log_operation(f"用户输入状态：{user_input}")



# 程序入口（标准写法）
if __name__ == "__main__":
    main()
