# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через контекст.

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def greeting():
    return 'Hello, world'


@app.route('/news/')
def news():
    context = [
        {'title': 'Врач перечислила способы пережить жару без последствий',
         'description': 'Если хотите пережить жару без последствий, ограничьте время нахождения на улице '
                        'с 11:00 до 16:00, так как в это время очень активное солнце.', 'date': '09-08-2023'},
        {'title':'От брюк и рубашки до кардигана: готовим ребенка к школе',
         'description': 'Это только кажется, что лето будет бесконечным, – на самом деле начало учебного '
                        'сезона уже совсем скоро. Чтобы подготовка к школе не застала вас врасплох и была максимально'
                        'продуктивной и приятной, предлагаем вам подумать о необходимых покупках заранее.',
         'date': '08-08-2023'}
    ]
    return render_template('news.html', news=context)


if __name__ == '__main__':
    app.run(debug=True)
