from flask import Flask, render_template,url_for
import json
app = Flask(__name__)
#
# @app.route('/<page_title>')
@app.route('/index/<page_title>')
def index(page_title):
    return render_template('base.html', title=page_title)

# @app.route('/<profession>')
@app.route('/trainings/<profession>')
def trainings(profession):
    return render_template('trainings.html', title=profession)

@app.route('/list_prof/<lst>')
def list_prof(lst):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']
    return render_template('list_prof.html', list=lst, professions=professions)






if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')