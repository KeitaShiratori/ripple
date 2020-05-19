from flask import Flask
import os

app = Flask(__name__)

from route.top import top
from route.prj import prj

app.register_blueprint(top)
app.register_blueprint(prj)

# sessionを有効にするための秘密鍵
app.secret_key = os.environ.get('SECRET_KEY')

if __name__ == '__main__':
  app.debug = True
  app.run(host='127.0.0.1',port=5000)
