from flask import Flask, render_template, request, make_response
from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response(render_template('readcookie.html', user = user))
    resp.set_cookie('userID', user)

    return resp
