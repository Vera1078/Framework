# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.


from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

app.secret_key = '5c297c9c7cc2c347e1df9e0027c3907aba9420bcfdb1cd54cb4f8a0c457ec8cc'
# сгенерировани с помощью secrets.token_hex() в строке интерпретаора Python


@app.route('/')
def greeting():
    return 'Hello, world'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        session['email'] = request.form.get('email') or 'NoEmail'
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('index'))

@app.route('/private_office/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('private_office.html')

if __name__ == '__main__':
    app.run(debug=True)
