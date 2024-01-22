#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"
@app.route("/print/<string:parameter>")
def print_string(parameter):
    info = f"{parameter}"
    print(info)
    return  info
@app.route("/count/<int:num>")
def count(num):
    numbers = "<h2>Counted Numbers:</h2>\n"
    for i in range(1, num + 1):
        numbers += f"<p>{i}</p>\n"
    return numbers

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1,operation,num2):
    if operation == "+":
        result = num1 + num2
        # return result
    elif operation == "-":
        result = num2 - num1
        # return result
    elif operation == "*":
        result =num1* num2
        # return result
    elif operation == "%":
        result = num2 % num1
        # return result
    else:
        return "Invalid Operation!"
    
    return f"<h2>Result of {num1} {operation} {num2} is {result}</h2>"




if __name__ == '__main__':
    app.run(port=5555, debug=True)
