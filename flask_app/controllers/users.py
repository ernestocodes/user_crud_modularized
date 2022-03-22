from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route('/users')
def users():
    users = User.get_all()
    return render_template('users.html', users=users)

@app.route('/users/new')
def new_user_form():
    return render_template('new_user.html')

@app.route('/user/create', methods=['POST'])
def create_user():
    print(request.form)
    User.create(request.form)
    return redirect('/users')

@app.route('/users/<int:id>')
def show(id):
    data = {
        'id':id
    }
    user = User.get_one(data)
    return render_template('show.html', user=user)

@app.route('/users/<int:id>/edit')
def edit(id):
    data = {
        'id':id
    }
    user = User.get_one(data)
    return render_template('update.html', user=user)

@app.route('/users/update', methods=['POST'])
def update():
    print(request.form)
    User.update_one(request.form)
    return redirect(f"/users/{request.form['id']}")

@app.route('/users/<int:id>/destroy')
def delete(id):
    data = {
        'id':id
    }
    User.delete_one(data)
    return redirect('/users')