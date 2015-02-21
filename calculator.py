from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


def calculate(operator1, operand, operator2):
    failure_text = "Calculation Failed: Use numbers."
    if operand == "+":
        try:
            result = float(operator1) + float(operator2)
        except:
            result = failure_text
    elif operand == "-":
        try:
            result = float(operator1) - float(operator2)
        except:
            result = failure_text
    elif operand == "/":
        try:
            result = float(operator1) / float(operator2)
        except:
            result = failure_text
    elif operand == "*":
        try:
            result = float(operator1) * float(operator2)
        except:
            result = failure_text
    else:
        result = "Operation Failed, operator probably unimplemented. Oops."
    return result


@app.route("/", methods=["GET", "POST"])
@app.route("/calculate/", methods=["GET", "POST"])
def calc_landing():
    if request.method == 'POST':
        result = calculate(request.form['operand1'], request.form['operator'],
                           request.form['operand2'])
        return render_template('main.html', result=result)
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
