from flask import session

def _set_data(key, data):
  if key in data:
    session[key] = data[key]

def set_session(data):
  _set_data('userID', data)
  _set_data('accessToken', data)
  _set_data('unix-timestamp', data)
  _set_data('seconds-until-token-expires', data)
  _set_data('signed-parameter', data)

def remove_session():
  session.clear()