from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/table/<int:age>/<sex>")
def colored_table(age, sex):
    # params = ageandsex.split("and")
    return render_template('table.html', member_age=age, member_sex=sex)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

