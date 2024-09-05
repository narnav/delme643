from flask import Flask, redirect, render_template, request, url_for
import sqlite3

con = sqlite3.connect("tutorial.db", check_same_thread=False)
api = Flask(__name__)
cur = con.cursor()
cur.execute("CREATE TABLE if not exists movie(title, year, score)")

@api.route('/', methods=['GET'])
def get_main():
    return render_template('main.html')

@api.route('/del', methods=['GET', 'POST'])
def del_data():
    if request.method == 'POST':
        # Extract the id of the item to be deleted from the form
        item_id = request.form['id']
        
        # Connect to your database (example with SQLite)
        con = sqlite3.connect('tutorial.db')
        cur = con.cursor()
        
        # Delete the item from the database
        cur.execute("DELETE FROM movie WHERE rowid = ?", (item_id,))
        con.commit()
        
        # Close the connection
        con.close()
        
        # Redirect to a different page or return a success message
        return redirect(url_for('show_data'))
    
    # For GET request, fetch all data to display
    con = sqlite3.connect('tutorial.db')
    cur = con.cursor()
    cur.execute("SELECT rowid,* FROM movie")
    data = cur.fetchall()
    con.close()
    
    return render_template('del.html', data=data)

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
