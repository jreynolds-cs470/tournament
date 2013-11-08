from flask import Flask, redirect, render_template, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Development Key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
db = SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('base.html')

@app.route('/site<num>')
def site(num):
    return render_template('site{0}.html'.format(num))


# Include a module runner to allow local testing
if __name__ == '__main__':
    app.run(debug=True)  # Set to false for production