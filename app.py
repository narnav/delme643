from flask import Flask, render_template, request
import sqlite3

con = sqlite3.connect("tutorial.db", check_same_thread=False)
api = Flask(__name__)
cur = con.cursor()
cur.execute("CREATE TABLE if not exists movie(title, year, score)")

@api.route('/', methods=['GET'])
def get_main():
    return render_template('main.html')

# TODO - add db connetion

@api.route('/add', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        score = request.form['score']
        cur.execute(f"INSERT INTO movie VALUES('{title}', {year}, {score})")
        con.commit()

        res = cur.execute("SELECT * FROM movie")
        return render_template('show.html',data=res.fetchall())
    else:
    
        return render_template('add.html')


@api.route('/show', methods=['GET'])
def show_data():
    res = cur.execute("SELECT * FROM movie")
    return render_template('show.html',data=res.fetchall())

if __name__ == '__main__':
    api.run(debug=True)
