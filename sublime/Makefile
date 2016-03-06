PWD = $(shell pwd)
USERDIR = $(HOME)/Library/Application\ Support/Sublime\ Text\ 2/Packages/User
COLORDIR = $(HOME)/Library/Application\ Support/Sublime\ Text\ 2/Packages/ColorScheme-User

install:
	ln -s $(PWD)/User/Make.sublime-build $(USERDIR)/C++\ Build.sublime-build
	ln -s $(PWD)/ColorScheme-User $(COLORDIR)

clean:
	rm -f $(USERDIR)/C++\ Build.sublime-build
	rm -rf $(COLORDIR)

all: clean install
