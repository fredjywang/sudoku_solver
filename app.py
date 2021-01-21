from flask import Flask, redirect, url_for, render_template, request, flash
from main import solve_board, valid_board

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
	return render_template("base.html")


@app.route("/sud_data", methods=["POST"])
def sud_data():
	if request.method == "POST":
		board = [
		[request.form["00"],request.form["01"],request.form["02"],request.form["03"],request.form["04"],request.form["05"],request.form["06"],request.form["07"],request.form["08"]],
		[request.form["09"],request.form["10"],request.form["11"],request.form["12"],request.form["13"],request.form["14"],request.form["15"],request.form["16"],request.form["17"]],
		[request.form["18"],request.form["19"],request.form["20"],request.form["21"],request.form["22"],request.form["23"],request.form["24"],request.form["25"],request.form["26"]],
		[request.form["27"],request.form["28"],request.form["29"],request.form["30"],request.form["31"],request.form["32"],request.form["33"],request.form["34"],request.form["35"]],
		[request.form["36"],request.form["37"],request.form["38"],request.form["39"],request.form["40"],request.form["41"],request.form["42"],request.form["43"],request.form["44"]],
		[request.form["45"],request.form["46"],request.form["47"],request.form["48"],request.form["49"],request.form["50"],request.form["51"],request.form["52"],request.form["53"]],
		[request.form["54"],request.form["55"],request.form["56"],request.form["57"],request.form["58"],request.form["59"],request.form["60"],request.form["61"],request.form["62"]],
		[request.form["63"],request.form["64"],request.form["65"],request.form["66"],request.form["67"],request.form["68"],request.form["69"],request.form["70"],request.form["71"]],
		[request.form["72"],request.form["73"],request.form["74"],request.form["75"],request.form["76"],request.form["77"],request.form["78"],request.form["79"],request.form["80"]]
		]
		if valid_board(board):
			solve_board(board)
			print(board)
			return render_template("solved.html", data=board)
		else:
			# invalid board; error message appears
			return redirect(url_for("index"))
	else:
		return redirect(url_for("index"))


@app.route("/home", methods=["POST"])
def home():
	if request.method == "POST":
		return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=5000)
