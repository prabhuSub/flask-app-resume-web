from flask import Flask, render_template, request, redirect
import smtplib
from email.message import EmailMessage
import os
import json

# vistor_count_file = open("static/vistor_count.json", "r")
# count_object = json.load(vistor_count_file)
# count_object["visitor_count"] = count_object["visitor_count"] + 1
# current_visitor_count = count_object["visitor_count"]
# vistor_count_file = open("static/vistor_count.json", "w")
# json.dump(count_object, vistor_count_file)
# vistor_count_file.close()

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    """this is to render index.html

    Returns:
        _type_: _description_
    """
    return render_template("index.html")

@app.route("/sendemail/", methods=['POST'])
def sendemail():
    """this is to use smtp of gmail to recieve emails form the users uing this email

    Returns:
        _type_: _description_
    """
    if request.method == "POST":
        name = request.form['name']
        subject = request.form['Subject']
        email = request.form['_replyto']
        message = request.form['message']

        # your_name = "Prabhu Subramanian"
        your_email = os.environ['flask_resume_web_app_email']
        your_password = os.environ['flask_resume_web_app_pass']

        # Logging in to our email account
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        # server.starttls()
        server.login(your_email, your_password)

        # Sender's and Receiver's email address
        sender_email =  "prabhus1652@gmail.com"
        receiver_email = "subramanian.pr@northeastern.edu"

        msg = EmailMessage()
        msg.set_content("\n---- Resume Flaks APP Message ----\n"+"First Name : "+str(name)+"\nEmail : "+str(email)+"\nSubject : "+str(subject)+"\nMessage : "+str(message))
        msg['Subject'] = 'New Response on Personal Website'
        msg['From'] = sender_email
        msg['To'] = receiver_email
        # Send the message via our own SMTP server.
        try:
            # sending an email
            server.send_message(msg)
        except Exception as e:
            pass
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
