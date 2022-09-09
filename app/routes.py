
from app import app
from flask import flash, redirect, render_template, url_for
from app.forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    user={'username': "dzw"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author':{'username':'Susan'},
            'body':'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title="Home",user=user,posts=posts)

@app.route('/login',methods=['get','post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.validate_on_submit())
        flash("Login Request from user {},  remember_me {}".format(form.username.data,form.remember_me.data))
        # print(get_flashed_messages())
        return redirect(url_for("index"))
        
    return render_template('login.html',title='Sign in',form=form)