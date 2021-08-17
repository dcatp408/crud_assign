from dojos_ninjas_app import app
from flask import render_template, redirect, request, session, flash
from dojos_ninjas_app.models.dojo import Dojo


@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos=dojos)


@app.route('/dojos/<int:user_id>')
def show_user(user_id):
    data = {
        "id": user_id
    }
    dojo = Dojo.dojo_with_ninjas(data)
    print(dojo.ninjas)
    return render_template("info.html", dojo=dojo)


@app.route('/dojos/create', methods=["POST"])
def dojo_():
    data = {
        "name": request.form["dojo_name"]
    }
    dojo = Dojo.save(data)
    return redirect('/dojos')
