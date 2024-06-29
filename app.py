from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = [{'username': 'test', 'password': 'test'}]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/flask_page')
def flask_page():
    return render_template('flask_1.html')

@app.route('/python_page')
def python_page():
    return render_template('python.html')

@app.route('/sql_page')
def sql_page():
    return render_template('sql.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the provided username and password match the single user in the list
    if users and users[0]['username'] == username and users[0]['password'] == password:
        return render_template('register.html', success='Login successful.')
    else:
        return render_template('register.html', error='Invalid username or password.')


if __name__ == '__main__':
    app.run(debug=True)
