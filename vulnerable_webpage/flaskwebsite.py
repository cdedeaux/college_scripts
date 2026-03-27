from flask import Flask, render_template, request, redirect, url_for
#learned through Flasks documentation at https://flask.palletsprojects.com/en/stable/tutorial/views/
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('sample.html')

@app.route('/action_page.php', methods=['POST'])
def login():
    username = request.form['uname'] 
    password = request.form['psw']    
    
    if username == 'trueadmin' and password == 'admin123':
        return redirect(url_for('success'))
    else:
        return redirect(url_for('failure'))

@app.route('/success')
def success():
    return "Login successful! flag{you_found_the_enumeration_flag}"
@app.route('/administrator.txt')
def secret_file():
    return "trueadmin:admin123"
@app.route('/failure')
def failure():
    
    return redirect(url_for('home'))

@app.route('/crazyunfindablebackdoor')
def backdoor():
    return "Backdoor accessed! flag{you_found_the_backdoor_flag}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

