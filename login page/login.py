from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'secret':
        return 'Login Successful'
    else:
        return 'Login Failed'

if __name__ == '__main__':
    app.run()
