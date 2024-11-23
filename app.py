from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'asfdhjawehjfkhawjkefhk'

users = {}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    if email in users and users[email]['password'] == password:
        return redirect(url_for('shop'))
    else:
        flash("Invalid email or password. Please sign up first.")
        return redirect(url_for('index'))

@app.route('/signup')
def sign_up_form():
    return render_template('sign_up.html')

@app.route('/sign_up', methods=['POST'])
def sign_up():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    if email in users:
        flash("Email already registered. Please log in.")
        return redirect(url_for('index'))
    else:
        users[email] = {'username': username, 'password': password}
        flash("Sign up successful! You can now log in.")
        return redirect(url_for('index'))

@app.route('/shop')
def shop():
    return render_template('shop.html')

if __name__ == '__main__':
    app.run(debug=True)