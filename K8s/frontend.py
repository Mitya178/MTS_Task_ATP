from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
app.template_folder = '/opt/MTS_Task'


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        # Вычисление суммы чисел
        sum_response = requests.post(f'http://backend1-service:5051/sum', json={'num1': num1, 'num2': num2})
        sum_result = sum_response.json()

        # Вычисление перемножения чисел
        multiply_response = requests.post(f'http://backend2-service:5052/multiply', json={'num1': num1, 'num2': num2})
        multiply_result = multiply_response.json()

        return render_template('result.html', sum_result=sum_result, multiply_result=multiply_result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
