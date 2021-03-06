# -*- coding: utf-8 -*-

from __future__ import unicode_literals

# This file is only used if you use `make publish` or explicitly specify it as
# your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://brunomaso1.github.io/blog'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
DISQUS_SITENAME = 'brunomaso1'
# GOOGLE_ANALYTICS = ""

ICONS.insert(0, ('feed', SITEURL + '/' + FEED_ALL_ATOM))
