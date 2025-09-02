# 代码生成时间: 2025-09-02 10:12:06
import gradio as gr
def validate_form(data):
    # 验证表单数据的函数
    # data: 包含表单数据的字典
    if 'name' not in data or not data['name'].strip():
        # 检查姓名是否为空
        raise ValueError('Name is required')
    if 'age' not in data or not 0 < data['age'] < 130:
        # 检查年龄是否在合理范围内
        raise ValueError('Age must be between 1 and 129')
    if 'email' not in data or '@' not in data['email']:
        # 检查电子邮件是否包含'@'
        raise ValueError('Invalid email format')
    return data  # 返回验证后的表单数据

def main():
    # 创建表单接口
    with gr.Interface(
        validate_form,
        inputs=[gr.Textbox(label='Name'),
                gr.Slider(minimum=1, maximum=130, label='Age'),
                gr.Textbox(label='Email')],
        outputs=['json'],
        examples=[['John Doe', 30, 'john@example.com'],
                  ['Jane Doe', 25, 'jane@example.com']],
        title='Form Data Validator',
        description='Validate form data using Gradio') as demo:
        demo.launch()

if __name__ == '__main__':
    main()