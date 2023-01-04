from flask import Flask
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! ?</p>"

@app.route('/hello/<name>')
def hello_name(name):
   return f'Hello {name}'

"""variable rules"""
@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

"""url building"""
@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

app.run(debug = True)