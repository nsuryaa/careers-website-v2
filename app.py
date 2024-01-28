from flask import Flask,render_template

#Creating object of class
app = Flask(__name__)

#Creating a route
@app.route("/")
def hello_world():
    return render_template('home.html')

print(__name__)
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)