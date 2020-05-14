from flask import Flask, render_template, request, Blueprint
from mw.prj import scan_prj

top = Blueprint('top', __name__, url_prefix='')

@top.route('/')
def index():
  data = scan_prj()
  return render_template('top.html', title='TOP', data=data)
