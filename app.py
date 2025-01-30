from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect('users.db')
    connection.row_factory = sqlite3.Row
    return connection

@app.route('/', methods=['GET', 'POST'])
def reg():
    message = None
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (login, password) VALUES (?, ?)', (login, password))
        conn.commit()
        conn.close()
        
        message = "Регистрация успешно завершена"
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)