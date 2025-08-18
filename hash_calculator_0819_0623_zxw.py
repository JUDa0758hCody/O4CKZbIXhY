# 代码生成时间: 2025-08-19 06:23:06
import hashlib
from gradio import graudio


# 哈希值计算工具类
class HashCalculator:
    def __init__(self):
        """初始化哈希计算器"""
        self.hash_functions = ['md5', 'sha1', 'sha256', 'sha512']

    def calculate_hash(self, input_text, hash_function):
        """计算给定文本的哈希值"""
        if hash_function not in self.hash_functions:
            raise ValueError(f'Unsupported hash function: {hash_function}
Supported functions: {self.hash_functions}')

        hash_obj = getattr(hashlib, hash_function)()
        hash_obj.update(input_text.encode('utf-8'))
        return hash_obj.hexdigest()


# 创建哈希计算器实例
hash_calculator = HashCalculator()


# 定义Graudio接口
def hash_interface(input_text, hash_function):
    """Graudio接口函数"""
    try:
        result = hash_calculator.calculate_hash(input_text, hash_function)
        return result
    except ValueError as e:
        return str(e)


# 创建Graudio界面
iface = graudio.Interface(
    fn=hash_interface,  # 指定接口函数
    inputs=["text", "select"],  # 输入参数
    outputs="text",  # 输出参数
    title="哈希值计算工具",  # 界面标题
    description="输入文本和选择哈希函数进行哈希值计算。"  # 界面描述
)

iface.launch()
