from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return render_template("base.html")
    
@app.route("/hello/<name>")
def hello_person(name):
    return render_template("template.html", name_string=name)
    
@app.route("/jedi/<firstname>/<lastname>")
def jedi(firstname, lastname):
    jediname = lastname[0:3] + firstname[0:2]
    return render_template("jedi_template.html", jediname=jediname, firstname=firstname, lastname=lastname)
        
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
            