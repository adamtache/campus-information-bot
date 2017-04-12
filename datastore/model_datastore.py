# -*- coding: utf-8 -*-
# Code modified from Google, licensed under the Apache License, Version 2.0

from flask import current_app
from google.cloud import datastore

def init_app(app):
    pass

def get_client():
    return datastore.Client(current_app.config['PROJECT_ID'])
