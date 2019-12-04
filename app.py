import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
import datetime
from flask_wtf import FlaskForm


app = Flask(__name__)

app.config["SECRET_KEY"] = 'the secret'
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

@app.route('/add_blog', methods=['GET', 'POST'])
def add_blog():
        wages=mongo.db.wages.find()
        regions=mongo.db.regions.find()
        parties=mongo.db.parties.find()
        religions=mongo.db.religion.find()
        ages=mongo.db.age_groups.find()
        return render_template("add_blog.html", ages=ages, regions=regions, wages=wages, parties=parties, religions=religions)

@app.route('/insert_blog', methods=['GET', 'POST'])
def insert_blog():
    
    now = datetime.datetime.now()
    
    blog= {
        "user_name":request.form.get("user_name"),
        "user_email":request.form.get("user_email"),
        "user_age":request.form.get("user_age"),
        "user_region":request.form.get("user_region"),
        "user_party":request.form.get("user_party"),
        "user_religion":request.form.get("user_religion"),
        "user_comment":request.form.get("user_comment"),
        "user_wage":request.form.get("user_wage"),
        "user_time":now
        }
    
    if request.method=="POST":
        blog = request.form.to_dict()
        user_profile = mongo.db.user_profile
        user_profile.insert_one(blog)
        flash('Your post has succeeded!')
    
    return redirect(url_for('user_blogs'))
    
    

    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
