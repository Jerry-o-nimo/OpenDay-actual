from flask import Flask, render_template, request, redirect, url_for
import xml.etree.ElementTree as ET

app = Flask(__name__)

# Load users from XML
def load_users():
    tree = ET.parse('users.xml')
    root = tree.getroot()
    users = {}
    for user in root.findall('user'):
        username = user.find('username').text
        password = user.find('password').text
        users[username] = password
    return users

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/after_login')
def after_login():
    return render_template('after_login.html')



@app.route('/authenticate', methods=['POST'])
def authenticate():
    users = load_users()
    username = request.form['email']
    password = request.form['password']
    
    if username in users and users[username] == password:
        return redirect(url_for('after_login'))
    else:
        return redirect(url_for('login'))

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/taskmaster')
def taskmaster():
    return render_template('tasks.html')

if __name__ == '__main__':
   # app.run(debug=True)
    app.run(host='0.0.0.0', port=6969, debug=False)
