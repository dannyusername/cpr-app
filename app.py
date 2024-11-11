from flask import Flask
from routes.accounts import accounts  # Import the blueprint

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

# Register the blueprint with a URL prefix
app.register_blueprint(accounts, url_prefix='/accounts')

if __name__ == '__main__':
    app.run(debug=True)

