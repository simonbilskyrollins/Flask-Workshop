from flask import Flask, render_template

app = Flask(__name__,
            template_folder='/Users/simonbr/Desktop/templated-linear',
            static_folder='/Users/simonbr/Desktop/templated-linear')


@app.route('/')
def hello():
    return render_template('index.html', subheading='Hello World!')

if __name__ == '__main__':
    app.run()
