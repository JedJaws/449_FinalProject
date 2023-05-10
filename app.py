from flask import Flask, render_template
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

online_users = mongo.db.users.find({"online": True})

@app.route("/")
def home():
    online_users = mongo.db.users.find({"online": True})
    return render_template("home.html", online_users=online_users)

@app.route("/about/")
def about():
    online_users = mongo.db.users.find({"online": True})
    return render_template("about.html", online_users=online_users)

@app.route("/contact/")
def contact():
    online_users = mongo.db.users.find({"online": True})
    return render_template("contact.html", online_users=online_users)

