from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/students')
def list_students():
    conn = sqlite3.connect('Lib_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    conn.close()
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)

