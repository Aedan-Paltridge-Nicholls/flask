from flask import Flask, redirect, url_for,request,render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("form.html")
@app.route('/welcome/<name>')
def Welcome(name):
    return f"<p>Hello,welcome  {name} </p>"

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == "POST":
        user = request.form['uname']
        return redirect(url_for('Welcome',name = user))
    else:
        user = request.args.get("uname")
        return redirect(url_for('Welcome',name = user))

if __name__ == '__main__':
    app.run(debug=True)