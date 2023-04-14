from flask import Blueprint, render_template
from .services.create_order import create_order

blueprint = Blueprint('orders', __name__)

@blueprint.route('/checkout', methods=['GET', 'POST'])
def checkout():
  cookies = Cookie.query.all()
  return render_template('orders/new.html', cookies=cookies)

@blueprint.post('/checkout')
def post_checkout():
  cookies = Cookie.query.all()
  return render_template('orders/new.html', cookies=cookies)

@blueprint.post('/checkout')
def post_checkout():
  # Create an order
  order = Order()
  order.save()

  cookies = Cookie.query.all()
  return render_template('orders/new.html', cookies=cookies)

address = Address(
  name=request.form.get('name'),
  street=request.form.get('street'),
  city=request.form.get('city'),
  state=request.form.get('state'),
  zip=request.form.get('zip'),
  country=request.form.get('country'),
  order=order
)
address.save()

@blueprint.post('/checkout')
def post_checkout():
  cookies = Cookie.query.all()

  create_order(request.form, cookies)

  return render_template('orders/new.html', cookies=cookies)


#data validation
@blueprint.post('/checkout')
def post_checkout():
  try:
    cookies = Cookie.query.all()

    if not all([
      request.form.get('name'),
      request.form.get('street'),
      request.form.get('city'),
      request.form.get('state'),
      request.form.get('zip'),
      request.form.get('country')
    ]):
      raise Exception('Please fill out all address fields.')

    create_order(request.form, cookies)
    return render_template('orders/new.html', cookies=cookies)
  except Exception as error_message:
    error = error_message or 'An error occurred while processing your order. Please make sure to enter valid data.'

    return render_template('orders/new.html', 
      cookies=cookies,
      error=error
    )