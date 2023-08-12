# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def square_number():
    if request.method == 'POST':
        num = int(request.form.get('num'))
        return f'{num}^2 = {num ** 2}'
    return render_template('result.html')



if __name__ == '__main__':
    app.run(debug=True)
