from app.extensions.databases import db, CRUDMixin

class Cookie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

class Dookie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(20), unique=True)
    title = db.Column(db.String(80))
    text = db.Column(db.Text())
   