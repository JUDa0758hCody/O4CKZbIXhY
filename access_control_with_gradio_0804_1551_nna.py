# 代码生成时间: 2025-08-04 15:51:02
import gradio as gr

# 模拟的用户数据库
class MockUserDatabase:
    def __init__(self):
        self.users = {
            "john": {"password": "john123", "role": "admin"},
            "jane": {"password": "jane123", "role": "user"},
        }

    def authenticate(self, username, password):
        """验证用户凭据"""
        user = self.users.get(username)
        if user and user["password"] == password:
            return user["role"]
        else:
            return None

# 权限控制函数
def access_control(role):
    """根据用户角色返回相应信息"""
    if role == "admin":
        return "Access granted: Admin privileges"
    elif role == "user":
        return "Access granted: Default privileges"
    else:
        return "Access denied: Unauthorized"

# 定义Gradio接口
def authenticate_user(username, password):
    """验证用户并返回权限"""
    db = MockUserDatabase()
    role = db.authenticate(username, password)
    if role:
        return access_control(role)
    else:
        return "Authentication failed: Invalid username or password"

# 创建Gradio界面
iface = gr.Interface(
    fn=authenticate_user,
    inputs=["text", "password"],
    outputs="text",
)

iface.launch()