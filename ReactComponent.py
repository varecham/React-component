import sublime
import sublime_plugin
import os
import functools


class reactcomponentCommand(sublime_plugin.WindowCommand):
	def run(self, dirs):
		self.window.show_input_panel("Component Name:", "", functools.partial(self.on_done, dirs[0]), None, None)

	def is_visible(self, dirs):
		return len(dirs) == 1

	def on_done(self, DName, CName):
		path = os.path.join(DName, CName)
		try:
			os.mkdir(path)

			index = open(os.path.join(path, "index.js"),"w+")
			index.write("export { default } from './%s'" % CName)
			index.close()

			cfile = open(os.path.join(path, ("%s.js" % CName)),"w+")
			cfile.write("import React from 'react';")
			cfile.close()

			self.window.open_file(os.path.join(path, ("%s.js" % CName)))
			print ("Component %s created" % CName)
		except OSError:
			print ("Error while creating component %s" % CName)