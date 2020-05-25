from flask import Flask, send_from_directory, session, request
import os

app = Flask(__name__)

from route.top import top
from route.prj import prj

app.register_blueprint(top)
app.register_blueprint(prj)

# sessionを有効にするための秘密鍵
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static/common/img'), 'favicon.ico', )

if __name__ == '__main__':
  app.debug = True
  app.run(host='127.0.0.1',port=5000)
