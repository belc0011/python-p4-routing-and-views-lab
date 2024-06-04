#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print(string)
    return string

@app.route('/count/<int:integer>')
def count(integer):
    range_list = []
    for num in range(integer):
        range_list.append(str(num))
    return '\n'.join(range_list) + '\n'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    int_num1 = int(num1)
    int_num2 = int(num2)
    if operation == '+':
        return str(int_num1 + int_num2)
    elif operation == '-':
        return str(int_num1 - int_num2)
    elif operation == "*":
        return str(int_num1*int_num2)
    elif operation == "div":
        return str(int_num1/int_num2)
    elif operation == "%":
        return str(int_num1%int_num2)

if __name__ == '__main__':
    app.run(port=5555, debug=True)