from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)
app.secret_key = 'pass'

from app import routes
