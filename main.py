from flask import Flask, request, redirect, render_template
import cgi 
import jinja2
import os


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['POST'])
def index_validation():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']


    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20 or " " in username:
        username_error='check the length of your username'

    if len(password) < 3 or len(password) > 20 or " " in password:
        password_error ='check the length of your password'

    if password != verify:
        verify_error='The users password and password-confirmation do not match.'

    if email != '':
        if len(email) < 3 or len(email) > 20 or " " in email or not (email.count('@') == 1) or not (email.count('.') == 1):
            email_error='not a valid email'

    if username_error or password_error or verify_error or email_error:
        return render_template('form.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=username, email=email)
    else:
        return render_template('welcome-page.html', username=username)
    
    
@app.route("/", methods=['GET'])
def index():

    
    return render_template('form.html')

app.run()