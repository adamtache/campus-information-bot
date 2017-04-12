# -*- coding: utf-8 -*-
# Code modified from Google, licensed under the Apache License, Version 2.0

from bot import get_model
from flask import Blueprint, redirect, render_template, request, url_for

crud = Blueprint('crud', __name__)

@crud.route('/add_restaurant', methods=['POST'])
def add_restaurant():
	data = request.restaurant.to_dict(flat=True)

	return get_model().create(data)

@crud.route('/<id>/edit_restaurant', methods=['POST'])
def edit_restaurant(id):
    restaurant = get_model().read(id)

    data = request.form.to_dict(flat=True)
    return get_model().update(data,'Restaurant', id)

@crud.route('/<id>/delete_restaurant')
def delete_restaurant(id):
    return get_model().delete('Restaurant', id)

@crud.route("/get_restaurants")
def get_restaurants():
    token = request.args.get('page_token', None)
    if token:
        token = token.encode('utf-8')

    restaurants, next_page_token = get_model().get(
    	limit=None, 
    	kind='Restaurant', 
    	cursor=token,
    )
    return restaurants


@crud.route('/<id>')
def get_restaurant(id):
    return get_model().read(id)
