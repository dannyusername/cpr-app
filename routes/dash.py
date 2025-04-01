# routes/dash.py
from flask import Flask, Blueprint, request, redirect, url_for, flash, render_template
import sqlite3
import bcrypt

dash = Blueprint('dash', __name__)

# Home route (protected content)
@dash.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
