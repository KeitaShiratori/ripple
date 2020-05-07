from flask import Flask, render_template, request, Blueprint

from mw.prj import parse, search_prj, get_prj, create_prj, update_prj

prj = Blueprint('prj', __name__, url_prefix='/prj')

@prj.route('/')
def index():
  return render_template('prj.html', title='Project検索', prj={})

@prj.route('/search', methods=['POST'])
def search():
  dto = parse(request)
  if dto is None:
    # 早期リターン
    return jsonify({'code': 'W00100','message': '入力された値が無効です。'})
  
  # 入力された条件でAWSのDBを検索
  data = search_prj(dto)

  # 検索結果を表示
  return jsonify({'data': data})

@prj.route('/show/<prj_id>', methods=['GET'])
def show(prj_id):
  if prj_id is None:
    # 早期リターン
    return render_template('prj_show.html', title='Project詳細', data={})
  
  # prj_idでAWSのDBを検索
  data = get_prj(prj_id)

  # 詳細ページを表示
  return render_template('prj_show.html', title='Project詳細', data=data)

@prj.route('/entry', methods=['GET'])
def entry():
  return render_template('prj_entry.html', title='Project作成')

@prj.route('/create', methods=['POST'])
def create():
  dto = parse(request)
  if dto is None:
    # 早期リターン
    return jsonify({'code': 'W00100','message': '入力された値が無効です。'})

  # prjを更新、更新後の情報をprjに再セット
  data = create_prj(dto)

  # 詳細ページを表示
  return render_template('prj_show.html', title='Project詳細', data=data, message='プロジェクトを作成しました。')


@prj.route('/update', methods=['POST'])
def update():
  dto = parse(request)
  if dto is None:
    # 早期リターン
    return jsonify({'code': 'W00100','message': '入力された値が無効です。'})
  
  # prj_idでAWSのDBを検索
  data = get_prj(dto.prj_id)
  if dto.user not in data.members:
    # 早期リターン
    return jsonify({'code': 'W00200','message': '更新権限がありません。'})

  # prjを更新、更新後の情報をprjに再セット
  data = update_prj(data, dto)

  # 詳細ページを表示
  return render_template('prj_show.html', title='Project詳細', data=data, message='プロジェクトを更新しました。')
