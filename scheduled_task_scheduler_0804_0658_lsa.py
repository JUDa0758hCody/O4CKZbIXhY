# 代码生成时间: 2025-08-04 06:58:35
import gradio as gr
# 添加错误处理
import schedule
# 增强安全性
import time
from threading import Thread

"""
定时任务调度器
# FIXME: 处理边界情况
使用GRADIO框架创建一个简单的定时任务调度器
# 扩展功能模块
支持添加任务、删除任务、查看任务列表等功能
"""

# 定时任务存储
task_list = {}

# 任务列表显示组件
# NOTE: 重要实现细节
task_list_component = gr.Markdown("## 任务列表")

# 添加任务函数
def add_task(name, interval):
    """添加定时任务
    Args:
        name (str): 任务名称
        interval (int): 任务间隔（秒）
    """
    global task_list
# 扩展功能模块
    if name in task_list:
        return "任务已存在"
    task_list[name] = schedule.every(interval).seconds.do(job, name)
    return f"任务 {name} 添加成功"

# 删除任务函数
def remove_task(name):
    """删除定时任务
    Args:
        name (str): 任务名称
    """
    global task_list
    if name not in task_list:
        return "任务不存在"
    schedule.cancel_job(task_list[name])
    del task_list[name]
    return f"任务 {name} 删除成功"

# 更新任务列表显示
def update_task_list():
    """更新任务列表显示
    """
    global task_list
    task_list_str = "## 任务列表\
"
    for name, task in task_list.items():
        task_list_str += f"- {name}: 每 {task.trigger.interval} 秒执行一次\
"
    task_list_component.update(task_list_str)

# 任务执行函数
def job(name):
    "