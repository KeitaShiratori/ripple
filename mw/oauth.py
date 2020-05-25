from flask import session
import requests, os

def is_valid_auth(authResponse):
  url_string = "https://graph.facebook.com/v7.0/oauth/access_token" \
              + "?grant_type=fb_exchange_token" \
              + "&client_id=" + os.environ.get('FB_APP_ID') \
              + "&client_secret=" + os.environ.get('FB_APP_SECRET') \
              + "&fb_exchange_token=" + authResponse['accessToken']
  r_get = requests.get(url_string)

  return r_get.status_code == 200

def set_session(data):
  _set_data('userID', data['authResponse'])
  _set_data('accessToken', data['authResponse'])
  _set_data('unix-timestamp', data['authResponse'])
  _set_data('seconds-until-token-expires', data['authResponse'])
  _set_data('signed-parameter', data['authResponse'])
  _set_data('name', data)

def _set_data(key, data):
  if key in data:
    session[key] = data[key]

def remove_session():
  session.clear()