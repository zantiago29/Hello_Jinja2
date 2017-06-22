from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
def say_hi():
    return render_template("base.html")
    
@app.route("/hello/<name>")
def hello_person(name):
    return render_template("template.html", name_string=name)
    
@app.route("/jedi/<firstname>/<lastname>")
def jedi(firstname, lastname):
    jediname = lastname[0:3] + firstname[0:2]
  
    html = """
        <h1>
        Hello {} {}!
        </h1>
        <p>
        Your jedi name is: {}
        </p>
        """
    return html.format(firstname.title(), lastname.title(), jediname.title())
        

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
            