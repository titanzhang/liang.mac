PWD = $(shell pwd)
USERDIR = $(HOME)/Library/Application\ Support/Sublime\ Text\ 3/Packages/User
COLORDIR = $(HOME)/Library/Application\ Support/Sublime\ Text\ 3/Packages/ColorScheme-User

install:
	ln -s $(PWD)/User/Make.sublime-build $(USERDIR)/C++\ Build.sublime-build
	ln -s $(PWD)/User/Preferences.sublime-settings $(USERDIR)/Preferences.sublime-settings
	ln -s $(PWD)/ColorScheme-User $(COLORDIR)

clean:
	rm -f $(USERDIR)/C++\ Build.sublime-build
	rm -f $(USERDIR)/Preferences.sublime-settings
	rm -rf $(COLORDIR)

all: clean install
