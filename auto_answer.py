from flask import Flask, render_template
app = Flask(__name__)
@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    params = {'tile': 'Анкета','surname':'Sosnovskaya','name':'Darya','education':'среднее','sex':'женщина','profession':'врач', 'motivation':')','ready':True}

    return render_template('auto_answer.html', **params)

if __name__ == '__main__':
    app.run(port = 8080, host='127.0.0.1')
