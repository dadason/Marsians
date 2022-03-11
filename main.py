from flask import Flask, render_template,url_for, request
import json
app = Flask(__name__)

@app.route('/<page_title>')
@app.route('/index/<page_title>')
def index(page_title):
    return render_template('base1.html', title=page_title)
@app.route('/<profession>')
@app.route('/training/<profession>')
def training(profession):

    return render_template('base2.html', title=profession)



#
# @app.route('/greeting/<username>')
# def greeting(username):
#     return render_template('base1.html', user=username, Title = username)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')