from email.mime.text import MIMEText
from subprocess import Popen, PIPE

# print(dir(MIMEText))
body = '''
<html><head></head>
<body>
<h1>Matcha</h1>
<p>Welcome to matcha. click the button to verify your email</p>
<a href="http://localhost:5000/verify?code=xxxxxx" >
<button type="button">verify</button>
</a>
</body>
</html>
'''
msg = MIMEText(body)
msg.set_type("text/html")
msg["From"] = "me@example.com"
msg["To"] = "adcada@mailinator.com"
msg["Subject"] = "This is the subject."
p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE, universal_newlines=True)
p.communicate(msg.as_string())
print("message")










