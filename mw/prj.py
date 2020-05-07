from flask import request

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
  return {
    'prj_id': 'prjid0001',
    'name': 'プロジェクト型マッチングサイト（仮名）の作成',
    'goal': 'StayHomeで余った時間を持ち寄って、ワクワクするプロジェクトを実践する場を作る',
    'issue': 'プロジェクト型のマッチングサイトは、フリーランスや副業などのビジネス色を全面に押し出したものばかり。カジュアルに友人とプロジェクトを実践する場がない。',
    'description': 'AWSとHerokuを使って、サービスを作る。\n・運用費は極限まで抑える\n・まずはプロジェクトを実践する過程を楽しむ\n・FBで一般の人にも楽しさが伝わるような活動報告をする',
    'start_date': '2020/05/06',
    'term': '1',
    'term_unit': 'ヵ月',
    'create_date': '2020/05/05',
    'timeline':[
      {
        'date_label': '2020/05/07',
        'event': '新規メンバー参画',
        'detail': 'サンプル太郎 さんがプロジェクトに参画しました'
      },
      {
        'date_label': '2020/05/08',
        'event': 'マイルストーン達成',
        'detail': '初めて動くサンプル画面を作成しました'
      }
    ]
  }

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
