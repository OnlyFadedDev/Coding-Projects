from flask import Flask, render_template

# python -m flask run
# ^ to run server

app = Flask(__name__)
print(__name__) # __main__
 
@app.route("/<username>/<int:post_id>") 
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id )

@app.route("/about.html") 
def about():
    return render_template('about.html')

@app.route("/favicon.ico") 
def blog():
    return "These are my thoughts on blogs"

@app.route("/blog/2020/dogs") 
def blog2():
    return "This is my dog"