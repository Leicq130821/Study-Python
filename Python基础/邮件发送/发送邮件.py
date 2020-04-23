from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP
# 实例化邮件内容对象。
Email=MIMEMultipart()
# 添加头部信息的标题信息。
Email['Subject']=Header('邮件标题')
# 添加发件人标识。
Email['From']='Python自动发'
# 添加收件人，多个收件人需要用逗号进行隔开。
Receivers=['583870243@qq.com','1359881082@qq.com']
Email['to']=Header(','.join(Receivers))
# 添加抄送人，多个抄送人需要用逗号进行隔开。
Chaosongs=['583870243@qq.com','1359881082@qq.com']
Email['Cc']=Header(','.join(Chaosongs))
# 添加正文内容。
msg='我是正文内容'
Zhengwen=MIMEText(msg,'plain','utf-8')
Email.attach(Zhengwen)

# 实例化SMTP协议对象。
Smtp_server='smtp.qq.com'
Smtp_port=25
Smtp=SMTP(Smtp_server,Smtp_port)
# 登录邮箱。
User='2821644642@qq.com'
Password='acrcpkjqxbckdfbc'
Smtp.login(User,Password)
# 发送邮件。
Smtp.sendmail(User, Receivers+Chaosongs, Email.as_string())
# 退出邮箱。
Smtp.quit()