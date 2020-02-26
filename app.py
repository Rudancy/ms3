import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
import datetime
from flask_wtf import FlaskForm
from bson.objectid import ObjectId 
from os import path
if path.exists("env.py"):
  import env

app = Flask(__name__)

 
app.config ["SECRET_KEY"] = os.environ.get('SECRET_KEY')
app.config ["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["MONGO_DBNAME"] = 'vote_base'

mongo = PyMongo(app)
""""

intial view of project

"""
@app.route('/')
@app.route('/home')
def home():

    
    
    return render_template('home.html')

    


@app.route('/user_blogs')
def user_blogs():
    
    #read; allows the user to read the blog
    
    return render_template("user_blogs.html", blogs=mongo.db.user_profile.find())



@app.route('/add_blog', methods=['GET', 'POST'])
def add_blog():
    
    
    #finds current information in db and renders in html form
    
        
        wages=mongo.db.wages.find()
        regions=mongo.db.regions.find()
        parties=mongo.db.parties.find()
        religions=mongo.db.religion.find()
        ages=mongo.db.age_groups.find()
        comment=mongo.db.user_comment.find()
        
        return render_template("add_blog.html", comment=comment, ages=ages, regions=regions, wages=wages, parties=parties, religions=religions)
    


@app.route('/insert_blog', methods=['GET', 'POST'])
def insert_blog():
    
    #creates user_blog into DB
    
    now = datetime.datetime.now()
    
    user_exists = mongo.db.user_profile.find_one({'user_email': request.form['user_email']})
    
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
        if user_exists is None:
            
            
            
            #credit to https://www.youtube.com/watch?v=vVx1737auSE
            
            blog = request.form.to_dict()
            user_profile = mongo.db.user_profile
        
            user_profile.insert_one(blog)
            flash("Blog has been logged!", "success")
            return redirect(url_for("user_blogs"))
        
        else:
            flash("this Email is taken!", "danger")
            return redirect(url_for("add_blog"))
    
    
@app.route('/edit_blog/<user_profile_id>')
def edit_blog(user_profile_id):
    
    #finds current information of user in db and renders in html form
    
    user = mongo.db.user_profile.find_one({"_id": ObjectId(user_profile_id)})
    all_blogs=mongo.db.user_profile.find()
    wages=mongo.db.wages.find()
    regions=mongo.db.regions.find()
    parties=mongo.db.parties.find()
    religions=mongo.db.religion.find()
    ages=mongo.db.age_groups.find()
    comment=mongo.db.user_comment.find()
   
    
    
    return render_template('edit_blog.html',comment=comment, user=user, blog=all_blogs, ages=ages, regions=regions, wages=wages, parties=parties, religions=religions, user_profile_id=user_profile_id)

@app.route('/update_blog/<user_profile_id>', methods=['POST'])
def update_blog(user_profile_id):
    
    #updates new information
    
    user_profile = mongo.db.user_profile
    user_profile.update_one( {'_id': ObjectId(user_profile_id)},
    {'$set':
    {
        'user_name':request.form.get('user_name'),
        'user_email':request.form.get('user_email'),
        'user_age':request.form.get('user_age'),
        'user_region':request.form.get('user_region'),
        'user_party':request.form.get('user_party'),
        'user_religion':request.form.get('user_religion'),
        'user_comment':request.form.get('user_comment'),
        'user_wage':request.form.get('user_wage')
    }})
    return redirect(url_for('user_blogs'))
    

@app.route('/delete_blog/<user_profile_id>')
def delete_blog(user_profile_id):
    
    #delete function
    
    mongo.db.user_profile.remove({'_id': ObjectId(user_profile_id)})
    return redirect(url_for('user_blogs'))
    
    
    

    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
