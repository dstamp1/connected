# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
# from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

# name of database
# app.config['MONGO_DBNAME'] = 'Connected'

# URI of database
# app.config['MONGO_URI'] = 'mongodb+srv://ConnectedUser:bjfHkVFz8izNs6KW@cluster0.2crxe.mongodb.net/Connected?retryWrites=true&w=majority'

# mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@app.route('/postings')
def postings():
    return render_template('postings.html')
@app.route('/profile')
def profile():
    return render_template('profile.html')

