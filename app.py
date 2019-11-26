import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'vote_base'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tpa55@mycluster-qbgul.mongodb.net/vote_base?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("homepage.html")



@app.route('/user_blogs')
def get_blogs_page():
    return render_template("blogs.html", blogs=mongo.db.user_profile.find())
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
