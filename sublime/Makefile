PWD = $(shell pwd)
USERDIR = $(HOME)/Library/Application\ Support/Sublime\ Text\ 2/Packages/User

install:
	ln -s $(PWD)/User/Make.sublime-build $(USERDIR)/C++\ Build.sublime-build

clean:
	rm -f $(USERDIR)/C++\ Build.sublime-build

all: clean install
