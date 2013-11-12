from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

# @app.route('/')
# def index():
#     return redirect(url_for('static', filename='index.html'))

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/site<num>')
def site(num):
    return render_template('site{0}.html'.format(num))


# Include a module runner to allow local testing
if __name__ == '__main__':
    app.run(debug=True)  # Set to false for production