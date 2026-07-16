from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            op = request.form["operator"]

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    result = "Division by zero is not allowed."
                else:
                    result = num1 / num2
            else:
                result = "Invalid operator"

        except ValueError:
            result = "Please enter valid numbers."

    return f"""
    <html>
    <head>
        <title>Simple Calculator</title>
    </head>
    <body>
        <h2>Simple Calculator</h2>

        <form method="post">
            First Number:
            <input type="text" name="num1"><br><br>

            Operator:
            <select name="operator">
                <option value="+">+</option>
                <option value="-">-</option>
                <option value="*">*</option>
                <option value="/">/</option>
            </select><br><br>

            Second Number:
            <input type="text" name="num2"><br><br>

            <input type="submit" value="Calculate">
        </form>

        <h3>Result: {result}</h3>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
