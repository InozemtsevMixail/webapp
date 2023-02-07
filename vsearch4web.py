from flask import Flask, render_template, request, escape
import vsearch


app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/search4' , methods=['POST'])
def do_search() -> 'ppythihtml':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Здесь есть твои результатсы: '
    results = str(vsearch.search4latters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Найди буквы в слове!')


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Форм Дата', 'Ремот_аддр', 'Юзер_агент', 'Результатсы')
    return render_template('viewlog.html',
                           the_row_titles=titles,
                           the_data=contents,
                           the_title='Вью Лог')


if __name__ == '__main__':
     app.run(debug=True)


