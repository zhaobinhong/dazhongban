# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from .celery import app as celery_app

__all__ = ['celery_app']
__version__ = "v1.0"
