import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



class gmail_:
     def __init__(self,user,password,host,port,to_addr,body,subject,filename,usessl=False,attachfile=False):
         self.host=host
         self.port=port
         self.user=user
         self.password=password
         self.usessl=usessl
         self.to_addr=to_addr
         self.body=str(body)
         self.subject=str(subject)
         self.msg = MIMEMultipart()
         self.attach_file=attachfile
         if self.attach_file:

            self.filename=filename
     def connect(self):
         try:
           if self.usessl:
              self.server=smtplib.SMTP_SSL(self.host,int(self.port))
              self.server.ehlo()

           else:
              self.server = smtplib.SMTP(self.host, int(self.port))
              self.server.starttls()
         except Exception as e:
             print(e)

     def  auth_(self):
         try:
            self.server.login(self.user,self.password)
         except Exception as e:
            print(e)
     def prepare_mail(self):
         try:

            if self.attach_file:
               self.msg["From"] = self.user if self.user.endswith(".com") else "@".join(self.user, "gmail.com")
               self.msg["To"] = self.to_addr
               self.msg.attach(MIMEText(self.body, "plain"))
               attachment=open(self.filename,"rb")
               p = MIMEBase('application', 'octet-stream')
               p.set_payload((attachment).read())
               encoders.encode_base64(p)
               p.add_header('Content-Disposition', "attachment; filename= %s" % self.filename)
               self.msg.attach(p)
            else:
               self.msg["body"]=self.body
               self.msg["subject"]=self.subject
            self.msg=self.msg.as_string()
         except Exception as e:
             print(e)
     def sendmail(self):
         try:
            self.server.sendmail(self.user,self.to_addr,self.msg)
         except Exception as e:
            print(e)
