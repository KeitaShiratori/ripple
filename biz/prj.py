import requests
import os

api_endpoint = os.environ.get('API_ENDPOINT')
headers = {
  'x-api-key':os.environ.get('API_KEY')
}

def get(prj_id):
  r_get = requests.get(api_endpoint + '/prj/' + prj_id, headers=headers)
  return r_get.json()

def post(dic):
  r_post = requests.post(api_endpoint + '/prj', headers=headers, json=dic)
  return r_post.json()
