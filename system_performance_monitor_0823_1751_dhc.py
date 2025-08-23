# 代码生成时间: 2025-08-23 17:51:47
import psutil
import gr

"""
系统性能监控工具

该工具使用GRADIO框架创建一个简单的界面，用于监控和显示系统的性能指标。
"""

# 获取系统性能指标的函数
def get_system_performance():
    """
    获取当前系统的CPU使用率、内存使用量和磁盘使用量

    返回值：
        dict -- 包含系统性能指标的字典
    """
    try:
        # 获取CPU使用率
        cpu_usage = psutil.cpu_percent(interval=1)
        # 获取内存使用量
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        # 获取磁盘使用量
        disk = psutil.disk_usage('/')
        disk_usage = disk.percent
        return {
            "CPU Usage": cpu_usage,
            "Memory Usage": memory_usage,
            "Disk Usage": disk_usage,
        }
    except Exception as e:
        # 错误处理
        print(f"Error: {e}")
        return {}

# 创建GRADIO界面
iface = gr.Interface(
    fn=get_system_performance,
    inputs=[],
    outputs="text",
    title="System Performance Monitor",
    description="A tool for monitoring system performance."
)

# 运行GRADIO界面
iface.launch()