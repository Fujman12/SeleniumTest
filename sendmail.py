import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import datetime
fromaddr = "bloginvestmonitor@gmail.com"

### TO Address
toaddr = "Fujman94@gmail.com"

def sendmail():
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Selenium PDF screenshot"

    body = "Please see attachment: \n"

    msg.attach(MIMEText(body, 'plain'))

    filename = "test_%s.pdf" % datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    attachment = open('test_%s.pdf' % datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"), "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "qwaqwa56")
    text = msg.as_string()
    print("Sending the e-mail...")
    server.sendmail(fromaddr, toaddr, text)
    print("E-mail sent")
    server.quit()
