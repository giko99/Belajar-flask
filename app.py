from sys import meta_path
from flask import Flask, render_template, request, session, sessions, url_for, redirect, request

app = Flask(__name__)
app.jinja_env.filters["zip"] = zip
app.config["SECRET_KEY"] = "ini secret key ku 2021"

@app.route("/", methods=["POST", "GET"])
def index():

    if "email" in session:
        return redirect(url_for("sukses_req"))
        # jika tombbol button di klik yg menyebabkan request post
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        print("email : ", email)
        print("password : ", password)
        # jika email dan password benar
        if email == 'admin@gmail.com' and password == 'pass':
            session['email'] = email
            session['password'] = password
            return redirect(url_for('sukses_req'))
        # jika email dan password salah
        else:
            return redirect(url_for('index'))

    return render_template("index.html")


@app.route("/sukses")
def sukses_req():
    dataJson ={
        "no": [1, 2, 3, 4, 5],
        "buah": ["mangga", "apel", "alpukat", "jeruk", "semangka"], 
        "hewan": ["ayam", "rusa", "buaya", "gajah", "kucing"], 
    }
    nilai = "Anda sukses login"
    return render_template("sukses.html", nilai=nilai, data=dataJson)


@app.route("/about")
def about():
    # jika dia sedang login
    if "email" in session:
        return render_template("about.html")
    # jika diat tidak sedang login
    else:
        return redirect(url_for('index'))


@app.route("/contact")
def contact():
    # jika dia sedang login
    if "email" in session:
        return render_template("contact.html")
    # jika diat tidak sedang login
    else:
        return redirect(url_for('index'))


@app.route("/logout")
def logout_akun():
    if "email" in session:
        session.pop("email")
        session.pop("password")
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


@app.route("/redirect-about")
def ayo_redirect_about():
    return redirect(url_for('about'))


@app.route("/redirect-contact")
def ayo_redirect_contact():
    return redirect(url_for('contact'))


if __name__ == "__main__":
    app.run(debug=True, port=5001)
