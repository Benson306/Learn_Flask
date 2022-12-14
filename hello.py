from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/home')
def index():
   return render_template("index.html")

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

@app.route('/success/<name>')
def success(name):
     return "welcome %s" % name

@app.route('/login', methods = ['POST','GET'])
def login():
     if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name= user))
     else:
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))

@app.route('/hello/<user>')
def hello_name(user):
   return render_template("hello.html", name = user)

@app.route('/marks/<int:score>')
def marks(score):
   return render_template('marks.html', marks = score)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60, 'maths':70}
   return render_template('result.html', result = dict)

@app.route('/input',methods = ['POST', 'GET'])
def new_result():
   if request.method == 'POST':
      result = request.form
      return render_template("show_results.html",result = result)

def hi_ben():
   return "Sasa Ben"

def newbie():
   return "Noobie"

app.add_url_rule('/ben','ben', hi_ben)
app.add_url_rule('/noobie','noobie', newbie)

if __name__ == '__main__':
   app.run(debug = True)
