from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route('/')
def home_page():
	"""Shows home page with a form asking for user input."""
	return render_template('form.html')

@app.route('/story')
def story():
	"""Shows completed madlib sotry."""
	place = request.form["place"]
	noun = request.form["noun"]
	verb = request.form["verb"]
	adj = request.form["adj"]
	pluralnoun = request.form["pluralnoun"]

	ans = {
		"place": place,
		"noun": noun,
		"verb": verb,
		"adj": adj,
		"pluralnoun": pluralnoun
	}

	story.generate(ans)


