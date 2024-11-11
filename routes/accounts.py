# routes/accounts.py
from flask import Flask, Blueprint, request, redirect, url_for, flash, render_template
import sqlite3
import bcrypt

accounts = Blueprint('accounts', __name__)

# Helper function to connect to the database
def get_db_connection():
    conn = sqlite3.connect("../cpr-db.sqlite")
    conn.row_factory = sqlite3.Row
    return conn

# Route for user registration
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Save the user in the database
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO user_data (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
            flash("Account created successfully!", "success")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Username already exists. Please choose another.", "error")
        finally:
            conn.close()
    return render_template('signup.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user_data WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            flash("Login successful!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password.", "error")
    return render_template('login.html')

# Home route (protected content)
@app.route('/home')
def home():
    return "Welcome to your dashboard!"

if __name__ == '__main__':
    app.run(debug=True)

