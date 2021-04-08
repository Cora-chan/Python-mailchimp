# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:25:04 2020

@author: Yue
"""


import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart;
from email.mime.image import MIMEImage;
from hardcode_png_pychart import hardcode_png_pychart;

hardcode_png_pychart();
FROMADDR = "kangyue9323@gmail.com"
LOGIN    = FROMADDR
PASSWORD = "Missgrandma"
TOADDRS  = ["kang.yue@sigmatm.com.au"]

#类型要muitipart
msg = MIMEMultipart('related')
msg['To']=Header('test111')
msg['From']=Header('testt222')
msg['Subject']=Header('test3333')

#添加文本
msgText = MIMEText("lalallalalalallalal")
msg.attach(msgText)

#添加图片
file = open("testpychart.png", "rb")
img_data = file.read()
file.close()
img = MIMEImage(img_data)
img.add_header('Content-ID', 'dns_config') 
msg.attach(img)



# mail_msg ="""
# <p>天才小康康的html测试</p>
# <p><a href="http://www.runoob.com">this  a test link</a></p>
# """

# message = MIMEText(mail_msg,'html','utf-8')
# message['From']=Header("小康康",'utf-8')
# message['To']=Header("我",'utf-8')

# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')


server = smtplib.SMTP('smtp.gmail.com', 587)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(LOGIN, PASSWORD)
server.sendmail(FROMADDR, TOADDRS, msg.as_string())
server.quit()











