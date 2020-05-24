from flask import request
from hashlib import blake2b
from datetime import datetime
import biz.prj as prj

def scan_prj():
  """
  プロジェクトを全件取得する
  """
  return prj.get('')

def get_prj(prj_id, user_id):
  """
  指定されたプロジェクトIDのプロジェクトを取得する
  """
  data = prj.get(prj_id)
  if 'errorMessage' in data or 'errorType' in data:
    return None

  data['is_login'] = len(user_id) > 0
  data['is_joined'] = len(list(filter(lambda m: m['user_id'] == user_id, data['members']))) > 0
  data['is_leader'] = list(filter(lambda m: m['member_type'] == 'leader', data['members']))[0]['user_id'] == user_id

  return data

def _make_prj_id(dat):
  h = blake2b(digest_size=8)
  h.update(dat.encode())
  return "prj_"+h.hexdigest()

def create_prj(data):
  """
  入力された情報でプロジェクトを作成する
  """
  # 入力されたprj情報にprj_idと生成日時を付与する
  now = datetime.now()
  data['create_date'] = now.isoformat()
  data['start_date'] = "{}/{}/{}".format(now.year,now.month,now.day)
  data['prj_id'] = _make_prj_id(data['create_date'])
  data['members'] = [
    {
      'user_id': data['fbid'],
      'user_name': data['fbnm'],
      'member_type': 'leader'
    }
  ]
  del data['fbid'], data['fbnm']

  prj.post(data)
  return data['prj_id']

def update_prj(data, dto):
  """
  入力された情報でプロジェクトを更新する
  """
  return {
    'prj_id': 'prjid0001',
    'name': 'sample project',
    'goal': 'sample goal',
    'issue': 'sample issue',
    'description': 'sample description',
    'start_date': '2020/05/08',
    'term': '1',
    'term_unit': 'ヵ月',
    'create_date': '2020/05/07',
  }
