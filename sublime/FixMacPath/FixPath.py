# Cloned from https://github.com/int3h/SublimeFixMacPath
from __future__ import division, absolute_import, print_function, unicode_literals
import sublime, sublime_plugin
import re, platform
from os import environ
from subprocess import Popen, PIPE


def isMac():
	if platform.system() == "Darwin":
		return True
	else:
		return False


if isMac():
	fixPathSettings = None
	originalEnv = {}

	def getSysPath():
		command = "TERM=ansi CLICOLOR=\"\" SUBLIME=1 /usr/bin/login -fqpl $USER $SHELL -l -c 'TERM=ansi CLICOLOR=\"\" SUBLIME=1 printf \"%s\" \"$PATH\"'"

		# Execute command with original environ. Otherwise, our changes to the PATH propogate down to
		# the shell we spawn, which re-adds the system path & returns it, leading to duplicate values.
		sysPath = Popen(command, stdout=PIPE, shell=True, env=originalEnv).stdout.read()

		sysPathString = sysPath.decode("utf-8")
		# Remove ANSI control characters (see: http://www.commandlinefu.com/commands/view/3584/remove-color-codes-special-characters-with-sed )
		sysPathString = re.sub(r'\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]', '', sysPathString)
		sysPathString = sysPathString.strip().rstrip(':')

		# Decode the byte array into a string, remove trailing whitespace, remove trailing ':'
		return sysPathString



	def fixPath():
		currSysPath = getSysPath()
		# Basic sanity check to make sure our new path is not empty
		if len(currSysPath) < 1:
			return False

		environ['PATH'] = currSysPath

		for pathItem in fixPathSettings.get("additional_path_items", []):
			environ['PATH'] = pathItem + ':' + environ['PATH']

		return True


	def plugin_loaded():
		global fixPathSettings
		fixPathSettings = sublime.load_settings("Preferences.sublime-settings")
		fixPathSettings.clear_on_change('fixpath-reload')
		fixPathSettings.add_on_change('fixpath-reload', fixPath)

		# Save the original environ (particularly the original PATH) to restore later
		global originalEnv
		for key in environ:
			originalEnv[key] = environ[key]

		fixPath()


	def plugin_unloaded():
		# When we unload, reset PATH to original value. Otherwise, reloads of this plugin will cause
		# the PATH to be duplicated.
		environ['PATH'] = originalEnv['PATH']

		global fixPathSettings
		fixPathSettings.clear_on_change('fixpath-reload')


	# Sublime Text 2 doesn't have loaded/unloaded handlers, so trigger startup code manually, first
	# taking care to clean up any messes from last time.
	if int(sublime.version()) < 3000:
		# Stash the original PATH in the env variable _ST_ORIG_PATH.
		if environ.has_key('_ST_ORIG_PATH'):
			# If _ST_ORIG_PATH exists, restore it as the true path.
			environ['PATH'] = environ['_ST_ORIG_PATH']
		else:
			# If it doesn't exist, create it
			environ['_ST_ORIG_PATH'] = environ['PATH']

		plugin_loaded()



else:	# not isMac()
	print("FixMacPath will not be loaded because current OS is not Mac OS X ('Darwin'). Found '" + platform.system() + "'")
