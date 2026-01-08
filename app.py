from flask import Flask, render_template, request
from db import Database


app = Flask(__name__)
db = Database()


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration', methods = ['post'])
def perform_registration():
    name = request.form.get('name')
    age = request.form.get('age')
    phone = request.form.get('phone')
    education = request.form.get('education')
    email = request.form.get('email')
    password = request.form.get('password')
    # Here you would typically save the user data to a database
    response = db.insert(name, age, phone, education, email, password)
   
    if response == 1:
        return render_template('login.html', message="registration successful")
    else:
        return render_template('login.html', error="Email already exists! Please login")


@app.route('/perform_login', methods=['POST'])
def perform_login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = db.get_user(email)
    if not user or user.get('password') != password:
        return render_template('login.html', error="Invalid login credentials")


    # Successful login — pass user fields to template
    return render_template('perform_login.html', name=user.get('name'), email=user.get('email'), age=user.get('age'), phone=user.get('phone'), education=user.get('education'))


if __name__ == '__main__':
    app.run(debug=True)
