# 代码生成时间: 2025-08-15 00:14:41
import grradio
from functools import lru_cache

# 定义一个函数，用于模拟计算密集型任务
def compute_expensive_task(input_data):
    # 这里使用一个简单的计算来模拟一个计算密集型任务
    result = sum(i * i for i in range(10000)) + input_data
    return result

# 使用 lru_cache 来缓存函数的返回值，最大缓存大小为 128
@lru_cache(maxsize=128)
def cached_compute_expensive_task(input_data):
    return compute_expensive_task(input_data)

# 定义一个错误处理函数，用于处理输入错误
def handle_input_error(e):
    error_message = f"Error: {e}"
    return error_message

# 定义一个grradio界面，用于输入和显示结果
def create_ui():
    # 创建输入组件，接受整数类型的输入
    input_interface = grradio.Textbox(label='Enter an integer', placeholder='Enter an integer')
    # 创建输出组件，用于显示计算结果
    output_interface = grradio.Textbox(label='Result')
    # 创建一个函数，用于更新输出组件
    def update_output(input_data):
        try:
            result = cached_compute_expensive_task(int(input_data))
            output_interface.update(value=str(result))
        except ValueError as e:
            output_interface.update(value=handle_input_error(e))
    # 将输入组件与函数连接
    input_interface.change(update_output, inputs=input_interface, outputs=output_interface)
    # 返回grradio界面
    return grradio.Interface(fn=update_output, inputs=input_interface, outputs=output_interface)

# 创建并运行grradio界面
if __name__ == '__main__':
    cache_policy_ui = create_ui()
    cache_policy_ui.launch()