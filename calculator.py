from flask import Flask


app = Flask(__name__)

@app.route("/")
def landing():
    return "This page is under construction."


@app.route("/calculate/<operand1>/<operator>/<operand2>")
def calculate(operand1, operator, operand2):
    calculation = str(operand1) + str(operator) + str(operand2)
    return "Were you trying to calculate {}?".format(calculation)

@app.route("/calculate/", methods=["GET", "POST"])
def calc_landing():
    landing_text = """<div>Take options, see if we can pass them to the server.</div>
    <form action="." method="POST">
        <input type="text" name="operand1">
        <select>
            <option> -
            </option>
            <option> +
            </option>
        </select>
        <input type="text" name="operand2">

        <input type="submit" name="submit" value="Send">
    </form>"""
    return landing_text

if __name__ == '__main__':
    app.run(debug=True)
