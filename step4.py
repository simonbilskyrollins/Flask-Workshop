from flask import Flask, render_template, redirect, request, url_for, session

app = Flask(__name__)
app.secret_key = "ain't nobody gonna crack this"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = request.form
        name = form['name']
        key = form['key']
        user_info = {'name': name, 'key': key}
        session['user_info'] = user_info
        return redirect(url_for('secret'))
    return render_template('login.html')


@app.route('/')
def hello():
    return render_template('step4_index.html')


@app.route('/secret')
def secret():
    name = session['user_info']['name']
    return render_template('step4_secret.html',
                           name=name,
                           color='purple')

if __name__ == '__main__':
    app.run()
