from flask import flask
from auth.routes import auth_bp

app = Flask(__name__)
app.secret_key = 'abcdefg'


app.register_blueprint(account_bp, url_prefix='/account')

if __name__ == '__main__':
    app.run(debug=True)