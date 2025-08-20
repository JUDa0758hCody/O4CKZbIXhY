# 代码生成时间: 2025-08-20 17:03:56
import gradio as gr
import csv
import os

"""
CSV文件批量处理器
这个程序可以让用户上传一个或多个CSV文件，并将它们批量处理。
处理后的结果将返回给用户。
"""

def process_csv_files(input_csv_files):
    """
    处理CSV文件的函数
    
    参数:
        input_csv_files (list): 一个包含多个CSV文件的列表
    """
    processed_files = []
    for file in input_csv_files:
        try:
            filename = file.name
            # 确保文件是CSV格式
            if not filename.endswith('.csv'):
                raise ValueError(f'文件{filename}不是CSV格式')

            # 读取CSV文件内容
            with open(file, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                data = list(reader)
                
            # 这里可以添加自定义的处理逻辑
            # 例如，可以对数据进行某种转换或分析
            # 假设我们将每个单元格的内容转为大写
            processed_data = [[cell.upper() for cell in row] for row in data]
                
            # 将处理后的数据写回CSV文件
            processed_filename = f'processed_{filename}'
            with open(processed_filename, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(processed_data)
            
            processed_files.append(processed_filename)
        except Exception as e:
            print(f'处理文件{filename}时发生错误：{e}')
            continue
    
    return processed_files

# 定义Gradio界面
iface = gr.Interface(
    fn=process_csv_files,
    inputs=gr.inputs.CsvFile(label='选择CSV文件', type='file', multiple=True),
    outputs=gr.outputs.CsvFile(label='处理后的CSV文件', type='file', multiple=True),
    title='CSV文件批量处理器',
    description='上传一个或多个CSV文件，程序将批量处理这些文件，并返回处理后的结果。'
)

# 运行Gradio界面
iface.launch()