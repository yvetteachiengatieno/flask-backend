from app.cookies.models import Cookie
def test_cookies_renders_cookies(client):
  # Page loads and renders cookies
  new_cookie = Cookie(slug='blog_article', name='Blog articles')
  new_cookie.save()

  response = client.get('/cookies')
  
  assert b'blog article' in response.data
