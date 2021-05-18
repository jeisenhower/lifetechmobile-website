from flask import Flask, render_template, request
from models import Quotes, NewsLetterSubs
from database import engine, SessionLocal, SQLALCHEMY_DATABASE_URI, PRODUCTION_SQL_DATABASE_URI
import models
import datetime

models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# NOTE: I actually don't need this. This is used for generating tokens and things like that, which I don't need at the moment
app.config['SECRET_KEY'] = 'aslkdjfacnzcmfnbej32io26a4s4d1a2f31bd31bfv1xc32vb1xc3v1x31x3v1bc'

# ENV = 'prod'
#
# if ENV == 'dev':
#     app.debug = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# else:
#     app.debug = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = PRODUCTION_SQL_DATABASE_URI

app.debug = False
app.config['SQLALCHEMY_DATABASE_URI'] = PRODUCTION_SQL_DATABASE_URI

# TODO: Fix the URL's for the navigation bar in the html files. They currently go off of local host, which is not correct. I think
#  that may be what's causing the issue with deploying and using this web app successfully.


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/services")
def services():
    return render_template('services.html')


@app.route("/submit", methods=['POST'])
def submit():
    if request.method != 'POST':
        return render_template('services.html', message='Error: Unauthorized')
    session = SessionLocal()
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    creation_time = datetime.datetime.utcnow()
    if name == '' or email == '' or message == '':
        return render_template('services.html', message='Please enter required fields')
    q = Quotes(name=name, email=email, message=message, creation_time=creation_time)
    session.add(q)
    session.commit()
    return render_template('success.html')


@app.route("/subscribe", methods=['POST'])
def subscribe():
    if request.method != 'POST':
        return render_template('services.html', message='Error: Unauthorized')
    session = SessionLocal()
    print(request.form)
    email = request.form['email']
    creation_time = datetime.datetime.utcnow()
    prev_sub = session.query(NewsLetterSubs).filter_by(email=email).count()
    if prev_sub != 0:
        return render_template('services.html', message='You are already subscribed to our newsletter!')
    if email == '':
        return render_template('home.html', message='Please enter a valid email')
    sub = NewsLetterSubs(email=email, creation_time=creation_time)
    session.add(sub)
    session.commit()
    return render_template('subscribed_success.html')


if __name__ == '__main__':
    app.run()
