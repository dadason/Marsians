from flask import Flask, render_template
app= Flask(__name__)

@app.route('/distribution')
def cubtics():
    team_members={"team":
    [
    "Macron",
    "Oliver",
    "Simon",
    "Jerry",
    "Sam",
    "Pam",
    "Tim"
    ]
    }
    print(team_members)
    return render_template('cubrics.html', distribution =team_members,title='Размещение по каютам')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)