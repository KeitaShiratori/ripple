from flask import Flask, render_template, request, Blueprint, session, jsonify
from mw.prj import scan_prj
from mw.oauth import set_session
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

  url_string = "https://graph.facebook.com/v7.0/oauth/access_token"
  url_string = url_string + "?grant_type=fb_exchange_token"
  url_string = url_string + "&client_id=" + os.environ.get('FB_APP_ID')
  url_string = url_string + "&client_secret=" + os.environ.get('FB_APP_SECRET')
  url_string = url_string + "&fb_exchange_token=" + session['accessToken']
  r_get = requests.get(url_string)
  print(r_get)
  return jsonify({"status": "ok"})

@top.route('/privacy-policy')
def privacy_policy():
  return render_template('privacy_policy.html', title='Privacy Policy')
