#!/usr/bin/env python
# coding=utf-8
import sae

from application import application

app = sae.create_wsgi_app(application)