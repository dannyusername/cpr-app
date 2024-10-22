from flask import Blueprint, render_template, request, redirect, url_for, flash
import sqlite3
import bcrypt

account_bp = Blueprint('account', __name__)

DATABASE = '../db/cpr-db.sqlite'

# Get and return a connection to DATABASE
def get_db_conn():
    connection = sqlite3.connect(DATABASE)
    return connection

def hash_pass(password):
    hash_pass = bcrypt.hashpw(password.encode('utf-8'))
    print("Hashed pass! " + hash)

def verify_hash_pass(password, hash_password):
    return bcrypt.checkpw(password.encode('utf-8'), hash_password)

@account_bp.route('/signup', methods=['GET','POST'])
def new_user:
    if request.method == 'POST':
        email = request.form['email']
        username = request.form["username"]
        password = request.form["password"]
        
        connection = get_db_conn()
        cursor = connection.cursor()

        try:

            new_user_query = '''
            INSERT INTO user_data
            VALUES 
            '''

            cursor.execute

    
    




def existing_user:
    user = raw_input("Enter your username")
    password = raw_input("Enter your password")

    pass

