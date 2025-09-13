# 代码生成时间: 2025-09-13 15:08:29
import gradio as gr

# 模拟的用户数据库
users = {"admin": "admin123"}

# 用户登录函数
def login(username, password):
    """验证用户登录信息"""
    # 检查用户名和密码是否正确
    if username in users and users[username] == password:
        return "Login successful!"
    else:
        # 返回错误信息
        return "Invalid username or password"

# 创建Gradio界面
iface = gr.Interface(
    fn=login,
    inputs=["text", "password"],
    outputs="text",
    title="User Login System",
    description="Please enter your username and password to login."
)

# 运行Gradio应用
iface.launch()