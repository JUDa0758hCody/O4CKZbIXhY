# 代码生成时间: 2025-09-09 06:14:55
from gradio import Interface
import json

"""
JSON数据格式转换器类，用于将JSON数据转换为原始格式
"""
class JsonDataConverter:
    def __init__(self):
        """
        初始化函数，不需要参数
        """
        pass

    def convert_to_json(self, data):
        """
        将输入的数据转换为JSON格式
        
        参数:
        data (str): 待转换的数据字符串
        
        返回值:
        str: JSON格式的字符串
        
        异常:
        ValueError: 如果输入的数据不是有效的JSON字符串
        """
        try:
            return json.dumps(json.loads(data), indent=4)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON data") from e

    def convert_from_json(self, json_data):
        """
        将JSON格式的数据转换为原始格式
        
        参数:
        json_data (str): JSON格式的数据字符串
        
        返回值:
        str: 原始格式的字符串
        
        异常:
        ValueError: 如果输入的数据不是有效的JSON字符串
        """
        try:
            return json.dumps(json.loads(json_data), ensure_ascii=False)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON data") from e

"""
创建Gradio界面，使用JsonDataConverter类进行数据转换
"""
def create_gradio_interface():
    converter = JsonDataConverter()
    interface = Interface(
        fn=converter.convert_to_json,
        inputs="text",
        outputs="text",
        examples=["["example"]"],
        title="JSON Data Converter",
        description="Convert data to and from JSON format"
    )
    interface.launch()

if __name__ == "__main__":
    create_gradio_interface()