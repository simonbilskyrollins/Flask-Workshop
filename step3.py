from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', text='Hello World!')


@app.route('/secret')
def secret():
    return render_template('secret.html',
                           text='Oh no! You broke my super-duper security!',
                           color='red')

if __name__ == '__main__':
    app.run()
