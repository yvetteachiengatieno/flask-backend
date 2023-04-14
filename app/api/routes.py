from flask import Blueprint, jsonify
from os import environ

blueprint = Blueprint('api', __name__)

@blueprint.get('/api/v1/orders')
def orders():
  if environ.get('API_KEY') == request.args.get('key'):
    orders = Order.query.all()
    return jsonify(
      serialize_orders(orders)
    )
  else:
    return jsonify({'error': 'Invalid API key'}), 401