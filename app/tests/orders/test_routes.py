from app.orders.models import Order

def test_get_checkout_renders(client):
  # Page loads and renders checkout
  response = client.get('/checkout')
  assert b'Checkout' in response.data

def test_post_checkout_creates_order(client):
  # Creates an order record
  response = client.post('/checkout', data={
    'Travel-blog poster': '2',
    'name': 'Jane',
    'street': '123 Main St',
    'city': 'Anytown',
    'state': 'CA',
    'zip': '12345',
    'country': 'Candyland'
  })
  assert Order.query.first() is not None

  def test_post_checkout_creates_address(client):
  # Creates an address related to the order
  response = client.post('/checkout', data={
    'travel poster': '2',
    'name': 'Jane',
    'street': '123 Main St',
    'city': 'Anytown',
    'state': 'CA',
    'zip': '12345',
    'country': 'Candyland'
  })
  assert Address.query.first().order_id is 1
