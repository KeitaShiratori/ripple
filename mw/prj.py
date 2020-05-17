from flask import request
from hashlib import blake2b
from datetime import datetime
import biz.prj as prj

def scan_prj():
  """
  プロジェクトを全件取得する
  """
  return prj.get('')

def get_prj(prj_id):
  """
  指定されたプロジェクトIDのプロジェクトを取得する
  """
  return prj.get(prj_id)

def _make_prj_id(dat):
  h = blake2b(digest_size=8)
  h.update(dat.encode())
  return "prj_"+h.hexdigest()

def create_prj(data):
  """
  入力された情報でプロジェクトを作成する
  """
  # 入力されたprj情報にprj_idと生成日時を付与する
  data['create_date'] = datetime.now().isoformat()
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
