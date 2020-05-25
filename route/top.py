from flask import Flask, render_template, request, Blueprint, session, jsonify
from mw.prj import scan_prj
from mw.oauth import is_valid_auth, set_session, remove_session

top = Blueprint('top', __name__, url_prefix='')

@top.route('/')
def index():
  data = scan_prj()
  session['referer'] = '/'
  return render_template('top.html', title='TOP', data=data)

@top.route('/oauth', methods=['POST'])
def oauth():
  if request is None or request.json is None or "authResponse" not in request.json:
    return
  
  json = request.json
  if is_valid_auth(json['authResponse']):
    set_session(json)

  return jsonify({"status": "ok"})

@top.route('/logout', methods=['POST'])
def logout():
  remove_session()
  return jsonify({"status": "ok"})

@top.route('/privacy-policy')
def privacy_policy():
  session['referer'] = '/privacy-policy'
  return render_template('privacy_policy.html', title='Privacy Policy')
