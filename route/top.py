from flask import Flask, render_template, request, Blueprint, session, jsonify
from mw.prj import scan_prj
from mw.oauth import set_session, remove_session
import requests, os

top = Blueprint('top', __name__, url_prefix='')

@top.route('/')
def index():
  data = scan_prj()
  return render_template('top.html', title='TOP', data=data)

@top.route('/oauth', methods=['POST'])
def oauth():
  if request is None or request.json is None or "authResponse" not in request.json:
    return
  
  set_session(request.json['authResponse'])

  url_string = "https://graph.facebook.com/v7.0/oauth/access_token" \
               + "?grant_type=fb_exchange_token" \
               + "&client_id=" + os.environ.get('FB_APP_ID') \
               + "&client_secret=" + os.environ.get('FB_APP_SECRET') \
               + "&fb_exchange_token=" + session['accessToken']
  r_get = requests.get(url_string)
  return jsonify({"status": "ok"})

@top.route('/logout', methods=['POST'])
def logout():
  remove_session()
  return jsonify({"status": "ok"})

@top.route('/privacy-policy')
def privacy_policy():
  return render_template('privacy_policy.html', title='Privacy Policy')
