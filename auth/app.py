from flask import Flask, request, render_template
from werkzeug.security import generate_password_hash, check_password_hash
import requests

raw_password = 'password'
HASHED_PASSWORD = generate_password_hash(raw_password, method='sha256')

app = Flask(__name__)

authenticated = False

@app.route('/auth-app/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        username = request.form['username'];
        password = request.form['password'];
        if username == 'Mircea' and check_password_hash(HASHED_PASSWORD, password):
            response = requests.get('http://ce ma fac? :(')
            return response.text
        else:
            return "Login failed"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
