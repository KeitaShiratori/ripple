from werkzeug.utils import secure_filename
import biz.img as img
import random, string, io, base64

# アップロードされる拡張子の制限
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
ALLOWED_MEMTYPES = set(['image/png', 'image/jpg', 'image/jpeg'])

def _allowed_file(photo):
  return '.' in photo.filename and photo.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS \
    and photo.mimetype in ALLOWED_MEMTYPES

def _randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

def upload_img(photo):
  if not _allowed_file(photo):
    return None

  photo_id = _randomname(32) + '.' + photo.filename.rsplit('.', 1)[1].lower()
  img.post({
    'photo_id': photo_id,
    'binary': base64.b64encode(io.BufferedReader(photo).read()).decode('utf-8')
  })

  return photo_id

def get_img(photo_id):
  return img.get(photo_id)
