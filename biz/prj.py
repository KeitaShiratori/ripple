import requests
import pprint

base_url = 

item_id = r_post.json()['id']
print(item_id)
# 93ead2568150009de5f1

r_get = requests.get(url_items + '/' + item_id, headers=headers)

print(r_get.status_code)
# 200

pprint.pprint(r_get.json())