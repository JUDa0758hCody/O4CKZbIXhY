# 代码生成时间: 2025-08-24 22:20:52
import gr
from gr import Textbox, Numberbox, Checkbox, Radio, Dropdown
from gr import Label, Layout, Card

"""
表单数据验证器

使用GRADIO框架创建一个简单的表单数据验证器
"""

class FormValidator:
    def __init__(self):
        # 创建布局
        self.layout = Layout()
        self.layout.add_component(Label(value="姓名"))
        self.layout.add_component(Textbox(label="姓名", placeholder="请输入姓名"))
        self.layout.add_component(Label(value="年龄"))
        self.layout.add_component(Numberbox(label="年龄", placeholder="请输入年龄"))
        self.layout.add_component(Label(value="性别"))
        self.layout.add_component(Dropdown(label="性别", options=["男", "女"], value="男"))
        self.layout.add_component(Label(value="同意协议"))
        self.layout.add_component(Checkbox(label="同意协议", value=False))

    def validate(self, data):
        """
        验证表单数据
        """
        # 验证姓名
        if not data["姓名"].strip():
            return False, "姓名不能为空"

        # 验证年龄
        try:
            age = int(data["年龄"])
            if age < 0 or age > 120:
                return False, "年龄超出合理范围"
        except ValueError:
            return False, "年龄必须是整数"

        # 验证性别
        if data["性别"] not in ["男", "女"]:
            return False, "性别必须是男或女"

        # 验证同意协议
        if not data["同意协议"]:
            return False, "必须同意协议"

        return True, "验证通过"

    def run(self):
        """
        运行表单验证器
        """
        self.layout.run()
        while True:
            data = self.layout.get_data()
            success, message = self.validate(data)
            if success:
                print("验证通过: ", message)
                break
            else:
                print("验证失败: ", message)

if __name__ == "__main__":
    validator = FormValidator()
    validator.run()