from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)


@app.route('/')
def test():
	return render_template('tournament.html')




# Include a module runner to allow local testing
if __name__ == '__main__':
    app.run(debug=True)  # Set to false for production