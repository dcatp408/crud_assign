from flask import Flask, render_template, request, session, redirect
from users import Users
app = Flask(__name__)
app.secret_key = "something "


@app.route('/')
def index():
    user = Users.get_all()
    # print(users)
    return render_template("index.html", all_users=user)


@app.route("/new")
def newPage():
    return render_template("page2.html")


@app.route('/result', methods=['POST'])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    Users.save(data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
