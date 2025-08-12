# 代码生成时间: 2025-08-13 04:42:29
import gradio as gr
import re
from collections import Counter

# 定义文本文件内容分析器类
class TextFileAnalyzer:
    """分析文本文件内容的工具。"""

    def __init__(self):
        self.supported_extensions = {'txt'}

    # 分析文本文件内容
    def analyze_text(self, file):
        """分析文本文件内容，返回统计结果。

        参数:
        file (gr.File): 待分析的文本文件。

        返回:
        dict: 包含文本统计结果的字典。
        """
        if file is None:
            raise ValueError("No file provided.")
        
        if file.extension not in self.supported_extensions:
            raise ValueError(f"Unsupported file extension: {file.extension}. Only 'txt' is supported.")
        
        with open(file.name, 'r') as f:
            content = f.read()
            
        self._validate_content(content)
        
        # 统计单词数量
        words = self._count_words(content)
        
        # 返回统计结果
        return {'total_characters': len(content), 'total_words': len(words), 'word_frequencies': words}

    # 验证内容是否为有效文本
    def _validate_content(self, content):
        if not isinstance(content, str):
            raise TypeError("Content must be a string.")
        if not content.strip():
            raise ValueError("File is empty or contains only whitespace.")

    # 统计单词数量
    def _count_words(self, content):
        """统计文本中单词的数量。

        参数:
        content (str): 文本内容。

        返回:
        Counter: 包含单词频率的Counter对象。
        """
        # 使用正则表达式分割单词
        words = re.findall(r'\b\w+\b', content.lower())
        return Counter(words)

    # 将分析结果转换为字符串表示
    def __repr__(self):
        return "<TextFileAnalyzer>"

# 创建Gradio界面
iface = gr.Interface(
    func=lambda file: TextFileAnalyzer().analyze_text(file),
    inputs=gr.File(label="Upload a text file"),
    outputs=["text", "label"],
    examples=[["example.txt"]],
    title="Text File Content Analyzer"
)

# 运行界面
iface.launch()