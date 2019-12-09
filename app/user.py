# coding:utf-8

from flask import Blueprint, render_template, redirect, request, url_for

from models import db, Users
from utils import judgemember


user = Blueprint('user', __name__)


@user.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        repassword = request.form['repassword']

        errors = judgemember(name, email)
        if password != repassword:
            errors.append('两次密码输入不一致')
        if len(errors) > 0:
            return render_template('register.html', errors=errors)
        else:
            user = Users(name, email, password)
            db.session.add(user)
            db.session.commit()
            db.session.close()
            return redirect(url_for('views.home'))
    else:
        return render_template('register.html')
