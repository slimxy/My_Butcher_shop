from flask import Flask, render_template

# new 12/9/22
import sqlite3

conect =  sqlite3.connect ('database.db')
# conect.execute('CREATE TABLE student'( name TEXT, ))
# end new 12/9/22
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/service')
def service():
    return render_template('service.html')

if __name__ == "__main__":
    app.run(debug = True)



