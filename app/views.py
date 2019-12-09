# coding:utf-8

from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    name = 'flask'
    return render_template('home.html', name=name)

