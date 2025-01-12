from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello"
@app.route('/pass/<int:score>')
def passed(score):
    return "status : Passed | marks :"+ str(score)
@app.route('/fail/<int:score>')
def fail(score):
    return "status : Failed | marks :"+str(score)
@app.route('/results/<int:marks>')
def result(marks):
    res = ""
    if marks >= 50:
        res = "passed"
    else:
        res = "fail"

    return redirect(url_for(res,score = marks))

if __name__ == '__main__':
    app.run(debug = True)
