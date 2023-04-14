def test_cookie_delete(client):
  # deletes cookie
  cookie = Cookie(slug='chocolate-chip', name='Chocolate Chip', price=1.50)
  db.session.add(cookie)
  db.session.commit()

  def test_cookie_delete(client):
  # deletes cookie
  cookie = Cookie(slug='butter', name='Butter', price=1.50)
  db.session.add(cookie)
  db.session.commit()

  cookie.delete()

  deleted_cookie = Cookie.query.filter_by(slug='butter').first()
  assert deleted_cookie is None