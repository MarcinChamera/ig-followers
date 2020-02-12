from flask import render_template, request, redirect
from . import app
from InstagramFollowers.bot import InstaBot

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        return redirect('/ig')
    else:
        return render_template("index.html")        

@app.route('/ig', methods=['GET', 'POST'])
def ig():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        bot = InstaBot()
        bot.login(username, password)
        unfollowers = bot.get_unfollowers()
        bot.logout()
        bot.quit()
        return render_template("ig.html", unfollowers=unfollowers)
    else:
        return render_template("ig.html")

    
'''
git add InstagramFollowers/.* Procfile requirements.txt webapp.py
git commit -m "commit"
git push heroku master
'''