#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Donly'
SITENAME = u"MAG's Note"
SITESUBTITLE = u'iOS/macOS/IoT/Web/Game'

SITEURL = u'https://magicalboy.com'
FEED_DOMAIN = SITEURL
FEED_ATOM = u'atom.xml'

TIMEZONE = 'Asia/Hong_Kong'

DEFAULT_LANG = 'zh_CN'

# Blogroll
LINKS =  (('MAGICALBOY', 'https://magicalboy.com'),)

# Social widget
# SOCIAL = (('Github', 'https://github.com/donly'),)
SOCIAL = (
          ('icon-github', 'https://github.com/donly'),
          ('icon-envelope-alt', 'mailto:donly@magicalboy.com'),
          ('icon-rss', 'atom.xml'),
          )

DEFAULT_PAGINATION = 10

# THEME="bootstrap"
THEME = "pelican-cait" #gum pelican-cait pelipress svbtle

# Will use this information to create a GitHub ribbon.
#GITHUB_URL='http://repo.magicalboy.com/'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DATE_FORMATS = {'en': '%a, %d %b %Y','jp': '%Y-%m-%d(%a)',}
USE_FOLDER_AS_CATEGORY = False

DEFAULT_CATEGORY = (u'misc')

DISQUS_SITENAME = 'magsnote'

# The static paths you want to have accessible on the output path “static”.
# By default, Pelican will copy the “images” folder to the output folder.
# 静态目录
STATIC_PATHS = (['images'])
