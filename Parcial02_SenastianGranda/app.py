from flask import Flask, render_template, request

app = Flask(__name__)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

@app.route('/factorial/<int:number>')
def factorial_result(number):
    result = factorial(number)
    return render_template('result.html', number=number, result=result)

if __name__ == '__main__':
    app.run(debug=True)
