
from flask import render_template, request, session, redirect

from flask_app import app

from flask_app.models.users import Users


@app.route('/')
def index():
    user = Users.get_all()
    # print(users)
    return render_template("index.html", all_users=user)


@app.route('/add')
def add_user():
    return render_template("add.html")


@app.route('/users/<int:user_id>')
def show_user(user_id):
    data = {
        "id": user_id
    }
    user = Users.show(data)
    return render_template("users.html", user=user, user_id=user_id)


@app.route('/result', methods=['POST'])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    Users.save(data)
    return redirect("users.html")


@app.route("/users/<int:user_id>/update")
def edit_user(user_id):
    data = {
        "id": user_id
    }
    user = Users.show(data)
    return render_template("update.html", user_id=user_id, user=user)


@app.route('/user/<int:user_id>/update', methods=['POST'])
def update(user_id):
    data = {
        "id": user_id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    edit_user = Users.update(data)
    return redirect(f"/users/{data['id']}")


@app.route('/users/<int:user_id>/destroy')
def destroy(user_id):
    data = {
        "id": user_id
    }
    destroy_user = Users.destroy(data)
    return redirect('/')
