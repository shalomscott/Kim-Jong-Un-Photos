import os
from flask import Flask
app = Flask(__name__)

@app.route('/<receiver_name>/<receiver_email>')
def send_kim_mail(receiver_name, receiver_email):
    os.system('python ./main.py %s %s Scott %s smtp.gmail.com %s' % (receiver_name, receiver_email, os.environ['GMAIL_ADDR'], os.environ['GMAIL_PASS']))
    return 'Sent Email'