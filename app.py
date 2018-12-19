from flask import *
from flask_mail import *
import pickle
import socket
import mail


pickle_in = open("cred.pickle","rb")
p = pickle.load(pickle_in)

app = Flask(__name__)

app.config.update(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    #MAIL_SERVER = 'kidosol2256@gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_SSL = False,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = 'kidosol2256@gmail.com',
    MAIL_PASSWORD = p

)

mail = Mail(app)


# @app.route('/')
# def hello_world():
#     return render_template('index.html')

@app.route('/',methods=["GET", "POST"])
def send_mail():
    try:
        if request.method == "POST":

            name = request.form.get('name', 'uvuvwevwevwe')
            msg_title="message from {}".format(name)

            msg = Message(msg_title,
                      sender="kidosol2256@gmail.com",
                      recipients=["kidosol2256@gmail.com"])
            msgbody = request.form.get('message')
            msg.body = msgbody
            mail.send(msg)

            auto_name = request.form.get('name', 'uvuvwevwevwe')
            ema = request.form.get('email', 'kidosol2256@gmail.com')
            auto_title = "Thank You {}".format(auto_name)
            autorep = Message(auto_title,
                      sender="kidosol2256@gmail.com",
                      recipients=[ema])
            autobody = "Hello thank you for your enquiry/question I will make sure to get back to you as soon as possible"
            autorep.body = autobody
            mail.send(autorep)

            return render_template("index.html")
        else:
            return render_template("index.html")
    except Exception as e:
        return str(e)

# @app.route('/send')
# def send_email():
#     try:
        # msg = Message("msg title",
        #               sender="kidosol2256@gmail.com",
        #               recipients=[formemail])
        # msg.body = "hello arsham my question is kdbnvkwhsbvshdkbvshjbcsdhjvbdshjvbdshvjbdshjvb"
        # mail.send(msg)
        # return 'mail sent'
    #
    # except Exception as e:
    #     return str(e)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)