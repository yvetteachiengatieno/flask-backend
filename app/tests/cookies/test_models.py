from app.extensions.database import db
from app.cookies.models import Cookie
from app.extensions.database import db, CRUDMixin

def test_cookie_update(client):
  # updates cookie's properties

  def test_cookie_update(client):
  # updates cookie's properties
  cookie = Cookie(slug='chocolate-chip', name='Chocolate Chip', price=1.50)
  db.session.add(cookie)
  db.session.commit()

  def test_cookie_update(client):
  # updates cookie's properties
  cookie = Cookie(slug='chocolate-chip', name='Chocolate Chip', price=1.50)
  db.session.add(cookie)
  db.session.commit()

  cookie.name = 'Peanut Butter'
  cookie.save()

  def test_cookie_update(client):
  # updates cookie's properties
  cookie = Cookie(slug='chocolate-chip', name='Chocolate Chip', price=1.50)
  db.session.add(cookie)
  db.session.commit()

  cookie.name = 'Peanut Butter'
  cookie.save()

  updated_cookie = Cookie.query.filter_by(slug='chocolate-chip').first()
  assert updated_cookie.name == 'Peanut Butter'

  def delete(self):
  db.session.delete(self)
  db.session.commit()
  return



