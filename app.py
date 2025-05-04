---

### `app.py`

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user for demonstration
USER = {
    'username': 'admin',
    'password': 'password123'
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USER['username'] and password == USER['password']:
            return f"Welcome, {username}!"
        else:
            return "Invalid username or password", 401
    return render_template('login.html')
