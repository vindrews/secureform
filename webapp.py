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
    a = random.randrange(1, 100)
    word = request.form['word']
    number = request.form['number']
    response = ""

    if request.method == 'POST':
        if a >= 1 and a < 10:
            response = "*()*"+word[0:3]+number+word[3:10]+"!@!"
        elif a >=10 and a < 20:
            response = "+{}+"+word[0:3]+number+word[3:10]+"*$*"
        elif a >= 20 and a < 30:
            response = "~()~"+word[3:10]+number+word[0:3]+"=!="
        elif a >= 30 and a < 40:
            response = "^&^"+word[3:10]+number+word[0:3]+">.<!"
        elif a >= 40 and a < 50:
            response = "=+=+"+word[3:5]+number+word[0:10]+"!.!=]"
        elif a >= 50 and a < 60:
            response = word[3:10]+"!_!"+number+"!@#@!"+word[0:3]
        elif a >= 60 and a < 70:
            response = word[0:3]+"-_-"+number+"{}_{}"+word[3:10]
        elif a >= 70 and a < 80:
            response = word[3:10]+"{}-{}"+number+"!%%!"+word[0:3]
        elif a >= 80 and a < 90:
            response = word[3:10]+"^%%^"+number+"+:##:+"+word[0:3]
        elif a >= 90 and word <= 100:
            reponse = word[0:3]+"("+number+")"+"| |"+word[3:10]
        return render_template('response.html', response = response)
    else:
        response = "Uh oh! Something went wrong, try again."
        return render_template('response.html', response = response)

if __name__=="__main__":
    app.run(debug=False)
