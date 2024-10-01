#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index_route():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<text>')
def print_route(text):
    print(text)  
    return text

@app.route('/count/<int:num>')
def count_route(num):
    return '\n'.join(str(i) for i in range(num)) + '\n'

@app.route('/math/<int:num1>/<op>/<int:num2>')
def math_route(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == 'div':
        result = num1 / num2
    elif op == '%':
        result = num1 % num2
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
