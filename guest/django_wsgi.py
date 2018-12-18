#!/usr/bin/env python
# coding: utf-8
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysit.settings")

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
