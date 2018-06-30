from flask import Flask, session, render_template, request, redirect, url_for
from app import app

@app.route('/')
def index():
   if 'username' in session:
      username = session['username']
      return render_template('logged_as.html', username = username)

   return render_template('Not_logged.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    return render_template('login_form.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
