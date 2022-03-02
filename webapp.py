from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    word = input('word') 
    number = input('number')
    return("*()*"+word[0:3]+number+word[3:5]+"!@!")
 
        
render_response()
render_main()
        
        