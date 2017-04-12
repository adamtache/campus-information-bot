# -*- coding: utf-8 -*-
# Code modified from Google, licensed under the Apache License, Version 2.0

from flask import current_app
from google.cloud import datastore

def init_app(app):
    pass

def get_client():
    return datastore.Client(current_app.config['PROJECT_ID'])

def update(data, key, id=None):
    ds = get_client()
    if id:
        key = ds.key(key, int(id))
    else:
        key = ds.key(key)

    entity = datastore.Entity(
        key=key,
        exclude_from_indexes=['description'],
    )

    entity.update(data)
    ds.put(entity)
    return _from_datastore(entity)

create = update

def read(id, key):
    ds = get_client()
    key = ds.key(key, int(id))
    results = ds.get(key)
    return from_datastore(results)

def delete(key, id):
    ds = get_client()
    key = ds.key(key, int(id))
    ds.delete(key)
    return key

def get(limit=10, kind, sort_by_key, cursor=None):
    ds = get_client()

    query = ds.query(kind=kind, order=[sort_by_key])
    query_iterator = query.fetch(limit=limit, start_cursor=cursor)
    page = next(query_iterator.pages)

    entities = builtin_list(map(from_datastore, page))
    next_cursor = (
        query_iterator.next_page_token.decode('utf-8')
        if query_iterator.next_page_token else None,
    )

    return entities, next_cursor

def _from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        {id: id, prop: val, ...}
    """
    if not entity:
        return None
    if isinstance(entity, builtin_list):
        entity = entity.pop()

    entity['id'] = entity.key.id
    return entity
