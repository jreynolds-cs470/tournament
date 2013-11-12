from flask import Flask, redirect, render_template, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Development Key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
db = SQLAlchemy(app)

class Team(db.Model):
	name = db.Column(db.String, primary_key=True)
	seed = db.Column(db.Integer)
	region = db.Column(db.string)

	def __init__(self,name,seed,region):
		self.name = name
		self.seed = seed
		self.region = region

	def __repr__(self):
		return '{0.seed}. {0.name} ({0.region} Region)'.format(self)


@app.route('/')
def index():
	for region in ['Midwest', 'West', 'South', 'East']:
		teams = Team.query.filter_by(region=region).all()
		print region
		print teams
		page.append('<h1>' + region + '</h1>')
		page.append('<ul>')
		for team in teams:
			page.append('<li>' + str(team.seed) + '. ' + team_name + '</li>')
		page.append('</ul>')
	
	return '\n'.join(page)

@app.before_first_request
def init_db():
	db.create_all()

	with open('bracket.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			if len(row) == 1:
				region = row[0].strip():
				name = row[1].strip()
				team = Team(name, seed, region)
				db.session.add(team)
	db.session.commit()
	
if __name__ == '__main__':
    app.run(debug=True)  