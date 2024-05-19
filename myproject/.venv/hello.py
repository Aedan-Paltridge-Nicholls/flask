from flask import Flask, redirect, url_for

app = Flask(__name__)
#Admin
@app.route('/admin')
def Hello_Admin():
    return f"<p>Hello,  Admin!</p>"

#guest
@app.route('/guest/<guest>')
def Hello_guest(guest):
    return f"<p>Hello,  {guest} As a guest</p>"

#user
@app.route('/hello/<name>')
def hello_User(name):
    if name == 'admin':
        return redirect(url_for('Hello_Admin'))
    else:
        return redirect(url_for('Hello_guest', guest = name))


if __name__ == '__main__':
    app.run(debug=True)