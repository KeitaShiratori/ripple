from flask import Flask, redirect, url_for

app = Flask(__name__)

from route.top import top

app.register_blueprint(top)

if __name__ == '__main__':
  app.debug = True
  app.run(host='127.0.0.1',port=5000)
