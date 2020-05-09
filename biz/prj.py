import requests
import os

url_items = os.environ.get('API_ENDPOINT')
headers = {
  'x-api-key':os.environ.get('API_KEY')
}

def get(prj_id):
  r_get = requests.get(url_items + '/prj/' + prj_id, headers=headers)
  return r_get.json()
