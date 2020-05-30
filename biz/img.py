import requests
import os, base64

api_endpoint = os.environ.get('API_ENDPOINT')
headers = {
  'x-api-key':os.environ.get('API_KEY')
}

def get(photo_id):
  r_get = requests.get(api_endpoint + '/img/' + photo_id, headers=headers)
  return base64.b64decode(r_get.text)

def post(dic):
  r_post = requests.post(api_endpoint + '/img', headers=headers, json=dic)
  return r_post.json()
