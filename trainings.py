from flask import Flask, render_template,url_for, request
import json

app = Flask(__name__)
@app.route('/trainings/<profession>')
def trainings(profession):
    return render_template('trainings.html', title=profession)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')