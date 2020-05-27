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

def create_prj(data, user_id, user_name):
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
      'user_id': user_id,
      'user_name': user_name,
      'member_type': 'leader'
    }
  ]

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

def upd_prj(data):
  prj.post(data)
  return data['prj_id']

def join_prj(prj_id, user_id, user_name):
  # prj_idでAWSのDBを検索
  data = prj.get(prj_id)
  if 'errorMessage' in data or 'errorType' in data:
    return None

  is_joined = len(list(filter(lambda m: m['user_id'] == user_id, data['members']))) > 0

  if is_joined:
    # すでに参加済みのメンバーだった場合は、正常扱いで処理終了
    return prj_id

  data['members'].append({
    'member_type': 'member',
    'user_id': user_id,
    'user_name': user_name
  })

  event = {
    'event': '新規メンバー参画',
    'detail': '{} さんがプロジェクトに参加しました。'.format(user_name),
    'disclosure_range': 'public'
  }

  _add_timeline(data, event)
  data = upd_prj(data)
  return prj_id

def _add_timeline(data, event):
  today = datetime.now().strftime('%Y/%m/%d')

  if 'timeline' not in data:
    data['timeline'] = []
  
  today_events = list(filter(lambda dic: 'date_label' in dic and dic['date_label'] == today, data['timeline']))
  if len(today_events) == 0:
    # data['timeline']内に当日日付のdate_labelがない場合、date_labelとeventを追加する
    data['timeline'].append(  {
      'date_label': today,
      'events': [event]
    })
  else:
    # 当日日付のdate_labelがある場合、eventを追加する
    today_events[0]['events'].append(event)

def add_timeline(prj_id, form):
  # prj_idでAWSのDBを検索
  data = prj.get(prj_id)

  event = {
    'event': 'ユーザ入力イベント',
    'detail': form['detail'],
    'disclosure_range': 'public'
  }
  _add_timeline(data, event)
  data = upd_prj(data)
  return prj_id

def add_link(prj_id, form):
  # prj_idでAWSのDBを検索
  data = prj.get(prj_id)

  event = {
    'event': form['event'],
    'detail': "関連リンクに <a href='{}' target='_blank'>{}</a> が追加されました".format(form['link_url'],form['link_title']),
    'disclosure_range': form['disclosure_range']
  }
  _add_timeline(data, event)

  if 'links' not in data:
    data['links'] = []
  
  data['links'].append({
    'link_title': form['link_title'],
    'link_url': form['link_url'],
    'disclosure_range': form['disclosure_range']
  })

  data = upd_prj(data)
  return prj_id

def complete_prj(prj_id, form):
  # prj_idでAWSのDBを検索
  data = prj.get(prj_id)

  event = {
    'event': form['event'],
    'detail': "プロジェクトが完了しました",
    'disclosure_range': 'public'
  }
  _add_timeline(data, event)

  data['outcome'] = form['outcome']
  data['is_complete'] = True
  now = datetime.now()
  data['complete_date'] = now.isoformat()
  data['end_date'] = "{}/{}/{}".format(now.year,now.month,now.day)

  data = upd_prj(data)
  return prj_id
