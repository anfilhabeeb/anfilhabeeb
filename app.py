from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Username: {username}, Password: {password}")
        # In a real app, you'd validate credentials here
        return 'Login attempt processed. Check console for credentials.'
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
