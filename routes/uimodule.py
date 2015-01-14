#!/usr/bin/env python
# coding=utf-8

import os.path
import tornado.web

class HeaderModule(tornado.web.UIModule):
	"""Header's UI module"""
	def render(self, name, page = 1):
		return self.render_string('modules/header.html', name=name, page=page)

class LogoModule(tornado.web.UIModule):
	"""Logo's UI module"""
	def render(self):
		return self.render_string('modules/logo.html')

class FooterModule(tornado.web.UIModule):
	"""Footer's UI module"""
	def render(self):
		return self.render_string('modules/footer.html')

class SignModule(tornado.web.UIModule):
	"""Sign form's UI module"""
	def render(self, signup):
		return self.render_string('modules/sign.html', signup=signup)

ui_modules = {
	'Header': HeaderModule,
	'Logo': LogoModule,
	'Footer': FooterModule,
	'Sign': SignModule
}