#smtplib用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header

# 发信方的信息：发信邮箱，QQ邮箱授权码
from_addr = '发件方的邮箱地址'
# QQ授权码
password = '这里填写自己的授权码，不懂的请百度'

# 收信方邮箱
to_addr = '收件方邮箱地址'

# 发信服务器
smtp_sever = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain为纯文本) ,第三个参数为编码
msg = MIMEText('<h1 style="text-aglin:center;"> 我好想你啊，儿子，你上班了吗? </h1>','html','utf-8')

# 邮件头信息
msg['From'] = Header(from_addr,'utf-8')
msg['To'] = Header(to_addr,'utf-8')
msg['Subject'] = Header('亲爱的儿子 : ','utf-8')

# 开启发信服务,这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_sever)
server.connect(smtp_sever,465)

#登录发信邮箱
server.login(from_addr,password)
# 发送邮件
server.sendmail(from_addr,to_addr,msg.as_string())

# 关闭服务器
server.quit() 

