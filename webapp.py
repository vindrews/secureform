import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

app.secret_key=os.environ["SECRET_KEY"];

@app.route("/")
def render_main():

    return render_template('home.html')

@app.route("/page1", methods=['POST', 'GET'])
def render_page1():
    session["1stgame"]=request.form['1stgame']
    return render_template('page1.html')

@app.route("/page2", methods=['POST', 'GET'])
def render_page2():
    session["players"]=request.form['players']
    return render_template('page2.html')
    
@app.route("/page3", methods=['POST', 'GET'])
def render_page3():
    session["gameengine"]=request.form['gameengine']
    return render_template('page3.html')
    
@app.route("/page4", methods=['POST', 'GET'])
def render_page4():
    session["playername"]=request.form['playername']
    return render_template('page4.html')

@app.route("/response", methods=['POST', 'GET'])
def render_response():
    session["countto"]=request.form['countto']
    game = session['1stgame']
    players = session['players']
    engine = session['gameengine']
    name = session['playername']
    countto = session['countto']

    
    if game == "halflife1" and players == "9" and engine == "source" and name == "chell" and countto == "3":
        reponse = "Great job! You know your Valve games. You got 5/5 correct!"
    else:
        response = "Aw, you got some wrong! Try again?" 
    return render_template('response.html', response = response)

if __name__=="__main__":
    app.run(debug=False)
