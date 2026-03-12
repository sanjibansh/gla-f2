from flask import Flask, render_template
from list_students import get_students

app = Flask(__name__)

@app.route("/")
def students():
	return "welcome to flask"

@app.route("/school")
def fun():
	return "welcome to school GLA flask class of sem 4@@@@@@@@@@@@@@@@"

@app.route("/sec")
def detail():
	return "section-F"

@app.route("/students")
def  test_html():
	list_of_students = get_students()
	return render_template("test.html", los=list_of_students)



if __name__ == "__main__":
	app.run(debug=True)