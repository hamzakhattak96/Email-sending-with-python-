#!/usr/bin/env python
# coding: utf-8

# In[9]:


import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


# In[10]:


emailfrom = "hamza.khattak.9678@gmail.com"
emailto = "hamza.ahmed@affinitysuite.net"

fileToSend2 = "v2.csv"

username = "hamza.khattak.9678@gmail.com"
password = "knloyceggmdqiqas"


# In[11]:


msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "Schedule Mail For the report of V2"
msg.preamble = "Schedule Mail For the report of V2"


# In[12]:


ctype, encoding = mimetypes.guess_type(fileToSend2)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"

maintype, subtype = ctype.split("/", 1)

if maintype == "text":
    fp = open(fileToSend2)
    # Note: we should handle calculating the charset
    attachment = MIMEText(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "image":
    fp = open(fileToSend2, "rb")
    attachment = MIMEImage(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "audio":
    fp = open(fileToSend2, "rb")
    attachment = MIMEAudio(fp.read(), _subtype=subtype)
    fp.close()
else:
    fp = open(fileToSend2, "rb")
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)
attachment.add_header("Content-Disposition", "attachment", filename=fileToSend2)
msg.attach(attachment)

server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(username,password)
server.sendmail(emailfrom, emailto, msg.as_string())
server.quit()


# In[ ]:




