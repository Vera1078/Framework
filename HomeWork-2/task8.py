# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)

app.secret_key = '45900ccf9346ce9cf1c8134fcd055cde0444b843126c17ec5d3e785a01009075'
# сгенерировани с помощью secrets.token_hex() в строке интерпретора Python

@app.route('/')
def greeting():
    return 'Hello, world'

@app.route('/flashh/', methods=['GET', 'POST'])
def flashh():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('flashh'))
    return render_template('flashh.html')


if __name__ == '__main__':
    app.run()
