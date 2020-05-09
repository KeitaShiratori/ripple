from flask import request
import biz.prj as prj

def parse(request):
  """
  リクエストされたデータをパースする
  """
  req = request.json
  return {
    'prd_id': req['prd_id']
  }

def search_prj(dto):
  """
  検索条件にしたがってプロジェクトを検索する
  """
  return {
    'prjs': [
      {
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
    ]
  }

def get_prj(prj_id):
  """
  指定されたプロジェクトIDのプロジェクトを取得する
  """
  return prj.get(prj_id)

def create_prj(dto):
  """
  入力された情報でプロジェクトを作成する
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
