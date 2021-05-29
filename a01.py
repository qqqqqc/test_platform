from flask import Flask,render_template


app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/login')
def index():
    return render_template('login.html')

if __name__ == "__main__":
    print(__name__)
    setattr(app,'debug',True)
    app.run()

