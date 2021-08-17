
from dojos_ninjas_app import app
from flask import render_template, redirect, request, session, flash
from dojos_ninjas_app.models.ninja import Users
from dojos_ninjas_app.models.dojo import Dojo


@app.route('/ninjas')
def ninja_new():
    dojos = Dojo.get_all()
    return render_template("ninjas.html", dojos=dojos)


@app.route('/ninjas/create', methods=["POST"])
def ninja_create():
    data = {
        'first_name': request.form["first_name"],
        'last_name': request.form["last_name"],
        'age': request.form["age"],
        'dojo_id': request.form['dojo_id']
    }
    create_ninja = Users.save(data)
    return redirect(f"/dojos/{data['dojo_id']}")
