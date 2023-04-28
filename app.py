from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret phrase"

@app.route('/')
def home_page():
	"""Shows home page with a form asking for user input."""
	prompts = story.prompts #gets keys in Story class
	return render_template('form.html', prompts=prompts)

@app.route('/story')
def generate_story():
	"""Shows completed madlib story."""
	filled_story = story.generate(request.args)
	return render_template('story.html', filled_story=filled_story)



	# place = request.form["place"]
	# noun = request.form["noun"]
	# verb = request.form["verb"]
	# adj = request.form["adj"]
	# plural_noun = request.form["pluralnoun"]

	# ans = {
	# 	"place": place,
	# 	"noun": noun,
	# 	"verb": verb,
	# 	"adj": adj,
	# 	"pluralnoun": plural_noun
	# }


