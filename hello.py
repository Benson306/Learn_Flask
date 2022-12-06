from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/ben/<number>')
def benji(number):
   return "Hello %s!" % number

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return "Blog Number %d" % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return "Revision Number %f" % revNo

@app.route('/admin')
def hello_admin():
   return "Hello Admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
   return "Hello %s as Guest" % guest

@app.route('/user/<name>')
def hello_user(name):
   if name == "admin":
      return redirect_url(url_for("hello_admin"))
   else:
      return redirect_url(url_for("hello_guest",guest = name))
def hi_ben():
   return "Sasa Ben"

def newbie():
   return "Noobie"

app.add_url_rule('/ben','ben', hi_ben)
app.add_url_rule('/noobie','noobie', newbie)

if __name__ == '__main__':
   app.run(debug = True)
