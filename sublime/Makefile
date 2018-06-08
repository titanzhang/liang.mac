PWD = $(shell pwd)
PACKAGEDIR = $(HOME)/Library/Application\ Support/Sublime\ Text\ 3/Packages
USERDIR = $(PACKAGEDIR)/User
COLORDIR = $(PACKAGEDIR)/ColorScheme-User

install:
	ln -s $(PWD)/User/Make.sublime-build $(USERDIR)/C++\ Build.sublime-build
	ln -s $(PWD)/User/JavaScript.sublime-build $(USERDIR)/JavaScript.sublime-build
	ln -s $(PWD)/User/LaTeX.sublime-build $(USERDIR)/LaTeX.sublime-build
	ln -s $(PWD)/FixMacPath $(PACKAGEDIR)/FixMacPath
	ln -s $(PWD)/User/Preferences.sublime-settings $(USERDIR)/Preferences.sublime-settings
	ln -s $(PWD)/ColorScheme-User $(COLORDIR)

clean:
	rm -f $(USERDIR)/C++\ Build.sublime-build
	rm -f $(USERDIR)/JavaScript.sublime-build
	rm -f $(USERDIR)/LaTeX.sublime-build
	rm -f $(PACKAGEDIR)/FixMacPath
	rm -f $(USERDIR)/Preferences.sublime-settings
	rm -rf $(COLORDIR)

all: clean install
