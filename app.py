from flask import Flask
from routes.accounts import accounts  
from routes.dash import dash
from routes.info import info
from routes.metronome import metronome 
from routes.quizzes import quizzes

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

# Register the blueprint with a URL prefix
app.register_blueprint(accounts, url_prefix='/accounts')
app.register_blueprint(dash, url_prefix='/home')
app.register_blueprint(info, url_prefix='/info')
app.register_blueprint(metronome, url_prefix='/metronome')
app.register_blueprint(quizzes, url_prefix='/quizzes')

if __name__ == '__main__':
    app.run(debug=True)
