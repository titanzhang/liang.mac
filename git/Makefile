PWD = $(shell pwd)

install:
	cp $(PWD)/gitconfig $(HOME)/.gitconfig
	cp $(PWD)/gitignore.global $(HOME)/.gitignore.global
	git config --global core.excluesfile $(HOME)/.gitignore.global

clean:
	rm -f $(HOME)/.gitconfig
	rm -f $(HOME)/.gitignore.global

all: clean install
