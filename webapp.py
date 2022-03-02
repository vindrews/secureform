from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
import random
    a = random.randrange(1, 100)
    word = input('word') 
    number = input('number')
    
if a >= 1 and a < 10:
    return("*()*"+word[0:3]+number+word[3:5]+"!@!")
elif a >=10 and a < 20:
    return("+{}+"+word[0:3]+number+word[3:5]+"*$*")
elif a >= 20 and a < 30:
    return("~()~"+word[3:5]+number+word[0:3]+"=!=")
elif a >= 30 and a < 40:
    return("^&^"+word[3:5]+number+wprd[0:3]+">.<!")
elif a >= 40 and a <50
 
        
render_response()
render_main()
        
