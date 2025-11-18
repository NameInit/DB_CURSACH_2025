from flask import session, render_template, request, redirect, url_for
from model.model_route import model_route
from database.DBoperation import select_dict, tranzakt, insert
from validators.decorator import group_required
from cache.decorator import redis_cache
from . import bp_basket, provider

@bp_basket.route('/')
@group_required
def basket_main_handler():
	res=redis_cache(model_route)(provider, [], 'get_products', select_dict)
	basket_items=session.get('basket') or {}
	total = sum(float(item['price'])*int(item['quantity']) for item in basket_items.values())
	return render_template('basket_main.html', 
						 products=res.result, 
						 basket_items=basket_items,
						 total=total)

@bp_basket.route('/add/<int:product_id>', methods=['POST'])
@group_required
def basket_add_handler(product_id):
	res=model_route(provider, [product_id], 'get_product_by_id', select_dict)
	if not res.status:
		return redirect(url_for('bp_basket.basket_main_handler'))
	product = res.result[0]
	basket = session.get('basket') or {}
	if str(product_id) in basket:
		basket[str(product_id)]['quantity']+=1
	else:
		basket[str(product_id)]={
			'name': product['name'],
			'price': product['price'],
			'group': product['group'],
			'country': product['country'],
			'quantity': 1
		}
	session['basket'] = basket
	session.modified = True
	return redirect(url_for('bp_basket.basket_main_handler'))

@bp_basket.route('/remove/<int:item_id>', methods=['POST'])
@group_required
def basket_remove_handler(item_id):
	basket = session.get('basket', [])
	del basket[str(item_id)]
	session['basket'] = basket
	session.modified = True
	return redirect(url_for('bp_basket.basket_main_handler'))

@bp_basket.route('/update_quantity/<int:item_id>', methods=['POST'])
@group_required
def basket_quantity_handler(item_id):
	action = request.form.get('action')  # 'increase' или 'decrease'
	basket = session.get('basket') or {}
	
	if action == 'increase':
		basket[str(item_id)]['quantity']+=1
	elif action == 'decrease' and basket[str(item_id)]['quantity']==1:
		del basket[str(item_id)]
	elif action == 'decrease' and basket[str(item_id)]['quantity']!=1:
		basket[str(item_id)]['quantity']-=1
	
	session['basket'] = basket
	session.modified = True
	
	return redirect(url_for('bp_basket.basket_main_handler'))

@bp_basket.route('/clear', methods=['POST'])
@group_required
def basket_clear_handler():
	session['basket'] = dict()
	session.modified = True
	
	return redirect(url_for('bp_basket.basket_main_handler'))

@bp_basket.route('/checkout', methods=['POST'])
@group_required
def basket_order_handler():
	basket = session.get('basket') or {}
	if not basket:
		return redirect(url_for('bp_basket.basket_main_handler'))

	order_id = model_route(provider, [session['id']], 'insert_user_order', insert).result
	operation = list()
	params = list()
	for product_id in basket:
		operation.append('insert_user_list_order')
		params.append([basket[str(product_id)]['price']*basket[str(product_id)]['quantity'],order_id,product_id])

	model_route(provider,params,operation,tranzakt)

	session['basket'] = dict()
	session.modified = True
		
	return render_template("basket_order.html", order_id=order_id)