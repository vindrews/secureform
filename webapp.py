import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session
from markupsafe import Markup, escape

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
    response = ""

    if session['1stgame'] == "Half Life 1" and session['players'] == "9" and session['gameengine'] == "Source" and session['playername'] == "Chell" and session['countto'] == "3":
        response = response + "Great job! You know your Valve games. You got 5/5 correct!"
    elif session['1stgame'] != "Half Life 1" or session['players'] != "9" or session['gameengine'] != "Source" or session['playername'] != "Chell" or session['countto'] != "3": 
        response = response + Markup("You answered some questions wrong. You said that Valve's first game was " + session['1stgame'] + ", that there were "+ session['players'] + " playable characters in Team Fortress Two, that Valve's game engine was " + session['gameengine'] + ", that the player's name in Portal is " + session['playername'] + ", and that Valve can't count to " + session['countto'] + ". One or more of these was wrong. Would you like to try again?") 
    return render_template('response.html', response = response)

@app.route('/startOver')
def startOver():
    session.clear() 
    return redirect(url_for('render_main')) 
    
if __name__=="__main__":
    app.run(debug=False)
