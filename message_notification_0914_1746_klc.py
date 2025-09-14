# 代码生成时间: 2025-09-14 17:46:02
import gr

"""
消息通知系统，使用GRADIO框架创建。
该系统允许用户输入消息和接收者邮箱，
然后发送通知邮件。
"""

# 导入所需库
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 定义邮件服务器配置信息
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'
FROM_EMAIL = SMTP_USERNAME

# 定义发送邮件的函数
def send_email(to_email, subject, message):
    """
    发送邮件给指定的接收者
    :param to_email: 接收者邮箱
    :param subject: 邮件主题
    :param message: 邮件内容
    :return: None
    """
    try:
        # 创建邮件对象
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # 连接到SMTP服务器并发送邮件
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(FROM_EMAIL, to_email, msg.as_string())
            print(f'邮件已发送到 {to_email}')
    except Exception as e:
        print(f'发送邮件失败: {e}')

# 创建GRADIO界面
def message_notification_interface():
    """
    创建GRADIO界面
    :return: None
    """
    with gr.Blocks() as demo:
        gr.Markdown(
            """
            <h1 style='color:blue;'>消息通知系统</h1>
            """)
        message = gr.Textbox(label='消息内容')
        email = gr.Textbox(label='接收者邮箱')
        send_button = gr.Button(label='发送通知')

        # 定义发送按钮的回调函数
        def send_notification(message, email):
            if not message or not email:
                return '请输入消息内容和接收者邮箱'
            subject = '重要通知'
            send_email(email, subject, message)
            return '邮件发送成功'

        send_button.click(send_notification, inputs=[message, email], outputs='text')

    # 启动GRADIO界面
    demo.launch()

# 程序入口点
if __name__ == '__main__':
    message_notification_interface()