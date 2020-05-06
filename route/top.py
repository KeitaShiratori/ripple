from flask import Flask, render_template, request, Blueprint

top = Blueprint('top', __name__, url_prefix='')

@top.route('/')
def index():
  return render_template('top.html', title='TOP')
