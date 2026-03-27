from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import sys
class Database:
    def __init__(self, db_name = 'ips.db'):
        self.db_name = db_name
        try:
            connection = sqlite3.connect(self.db_name)

        except:
            print("Failed database connection.")

            
            sys.exit()
        cur = connection.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS ip(ip_address TEXT UNIQUE)")
        connection.commit()
        connection.close()

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('homepage.html')
@app.route('/showip')
def return_ip():
    user_ip = request.remote_addr
    db = Database()
    

    connection = sqlite3.connect(db.db_name, timeout=10)
    cur = connection.cursor()
    
    try:
        query = "INSERT INTO ip (ip_address) VALUES (?)"
        cur.execute(query, (user_ip,))
        connection.commit()
    except sqlite3.IntegrityError:
        pass
    finally:  
        connection.close()
    
    return render_template('frontend.html', ip_address=user_ip)
if __name__ == "__main__":
    website_url = 'not-a-suspicous-link:8080'
    app.config['SERVER_NAME'] = website_url
    app.run(debug=True, host='0.0.0.0')