# coding=utf-8
# 运用smtp协议发送邮件
# SMTP协议
# 提供可靠且有效的电子邮件传输的协议
# 协议客户端
# email负责构造邮件，smtplib负责发送邮件
import smtplib
# 创建文本内容的邮件体
from email.mime.text import MIMEText
from email.header import Header

import random

# sample()多用于截取列表的指定长度的随机数
sim=random.sample(list(range(9)),6)

# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
sim=list(map(lambda x:str(x),sim))
print(map(lambda x:str(x),sim))
sim=''.join(sim)



# QQ
mail_host = "smtp.qq.com"  # 设置服务器  smtp.163.com
mail_user = "1070727987@qq.com"  # 用户名
mail_pass = "jgvtbzuzgwhrbbdg"  # 口令
receivers = ['1070727987@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


# # 网易
# mail_host = "smtp.163.com"  # 设置服务器  smtp.163.com
# mail_user = "ahuangdegege@163.com"  # 用户名
# mail_pass = "NVJJDCUHVRGIYWBZ"  # 口令


# 第一个参数就是邮件正文
# 第二个参数是MIME的subtype，传入'plain'，最终的MIME就是'text/plain'
# 最后一定要用utf-8编码保证多语言兼容性
message = MIMEText('宝贝你的邮件来了,验证码是%s快来试试呦。' % sim, 'plain', 'utf-8')

# QQ
# # 发送者
message['From'] = Header("白志雄", 'utf-8')
# 接收者
message['To'] = Header("白志雄", 'utf-8')

# 网易
# message['From'] = "ahuangdegege@163.com"
# message['To'] = '781430965@qq.com'

# 标题
subject = '【Python SMTP 邮件测试】'
message['Subject'] = Header(subject, 'utf-8')
# 下面为发送代码段
try:
    smtpObj = smtplib.SMTP()
    # 设置服务器，端口号
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    # 设置登录账号
    smtpObj.login(mail_user, mail_pass)
    # print(mail_user, mail_pass)
    # 发送人， 接受人， 消息内容
    print(message.as_string())  # 返回一个字符串信息
    smtpObj.sendmail(mail_user, receivers, message.as_string())

    # 网易
    # smtpObj.sendmail(mail_user, receivers, message.as_string())

    print("邮件发送成功")
except:
    print('邮件发送失败')
    exit()

sim_1 = input('请输入您收到的验证码：')

if sim == sim_1:
    print('恭喜您输入的正确')
else:
    print("铁子，没门票想上车?")



