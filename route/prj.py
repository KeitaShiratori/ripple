from flask import Flask, render_template, request, Blueprint, session, redirect, url_for
from mw.prj import scan_prj, get_prj, create_prj, update_prj

prj = Blueprint('prj', __name__, url_prefix='/prj')

@prj.route('/')
def index():
  session['referer'] = '/prj'
  return render_template('prj/search.html', title='Project検索', prj={})

@prj.route('/show/<prj_id>', methods=['GET'])
def show(prj_id):
  if prj_id is None:
    # 早期リターン
    return render_template('prj/show.html', title='Project詳細', data={})

  # sessionからユーザ情報を取得
  user_id = session['userID'] if "userID" in session else ""

  # prj_idでAWSのDBを検索
  data = get_prj(prj_id, user_id)

  if data is None:
    # データが取得できなかった場合、
    return render_template('err/404.html', title='404 | 指定された情報が見つかりませんでした')

  # データが取得できた場合、sessionに参照しているプロジェクト情報をセットする
  session['LatestViewProjectId'] = prj_id
  session['referer'] = '/prj/show'

  # 詳細ページを表示
  return render_template('prj/show.html', title='Project詳細', data=data)

@prj.route('/entry', methods=['GET'])
def entry():
  session['referer'] = '/prj/entry'
  return render_template('prj/entry.html', title='Project作成', data=empty_data)

@prj.route('/create', methods=['POST'])
def create():
  data = dict(request.form)
  if 'name' not in data or len(data['name']) is 0:
    # 早期リターン
    return jsonify({'code': 'W00100','message': '入力された値が無効です。'})

  # # prjを更新、更新後の情報をprjに再セット
  prj_id = create_prj(data)

  session['referer'] = '/prj/create'
  # 詳細ページを表示
  return redirect(url_for('prj.show', prj_id=prj_id))


@prj.route('/update_entry/<prj_id>', methods=['GET'])
def update_entry(prj_id):
  if prj_id is None:
    # 早期リターン
    return render_template('prj/show.html', title='Project詳細', data={})

  # sessionからユーザ情報を取得
  user_id = session['userID'] if "userID" in session else ""

  # prj_idでAWSのDBを検索
  data = get_prj(prj_id, user_id)

  session['referer'] = '/prj/update_entry'
  # 詳細ページを表示
  return render_template('prj/update_entry.html', title='Project更新', data=data)

@prj.route('/update', methods=['POST'])
def update():
  dto = parse(request)
  if dto is None:
    # 早期リターン
    return jsonify({'code': 'W00100','message': '入力された値が無効です。'})
  
  # prj_idでAWSのDBを検索
  data = get_prj(dto.prj_id, user_id)
  if dto.user not in data.members:
    # 早期リターン
    return jsonify({'code': 'W00200','message': '更新権限がありません。'})

  # prjを更新、更新後の情報をprjに再セット
  data = update_prj(data, dto)

  session['referer'] = '/prj/update'
  # 詳細ページを表示
  return render_template('prj/show.html', title='Project詳細', data=data, message='プロジェクトを更新しました。')

@prj.route('/joinProject', methods=['GET'])
def joinProject():
  if session['referer'] is not '/prj/show':
    # プロジェクト参加が可能なのは、プロジェクト詳細ページからプロジェクト参加ボタンを押されたときのみ。
    return render_template('err/404.html', title='404 | 指定された情報が見つかりませんでした')

  user_id = session['userID'] if "userID" in session else ""
  prj_id = session['LatestViewProjectId'] if "LatestViewProjectId" in session else ""

  if user_id == "" or prj_id == "":
    # ユーザID、プロジェクトIDがなかったらプロジェクト参加処理を実行できないのでエラー
    return render_template('err/404.html', title='404 | 指定された情報が見つかりませんでした')

  # prj_idでAWSのDBを検索
  data = get_prj(prj_id, user_id)

  if data is None:
    # データが取得できなかった場合、
    return render_template('err/404.html', title='404 | 指定された情報が見つかりませんでした')
