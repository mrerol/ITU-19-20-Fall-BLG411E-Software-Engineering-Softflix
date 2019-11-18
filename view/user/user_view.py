from flask import render_template, redirect, url_for, request


def login():
    return render_template('user/login.html')
