from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
import smtplib 

#not used here but if needed to send an confirmation email

def send_ok(title,email,date,S_time):
    fromaddr = "XXXXX@gmail.com" ## a config https://myaccount.google.com/lesssecureapps
    toaddr = email
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] =title 
    msg.attach(MIMEText("You have an appointment the "+date+"at"+S_time,"html","utf-8")) 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls()  
    s.login(fromaddr, "XXXXX") 
    s.sendmail(fromaddr, toaddr, msg.as_string()) 
    s.quit() 