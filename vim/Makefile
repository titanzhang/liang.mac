PWD = $(shell pwd)

install:
	ln -s $(PWD) $(HOME)/.vim
	ln -s $(PWD)/vimrc $(HOME)/.vimrc

clean:
	rm -f $(HOME)/.vimrc
	rm -fr $(HOME)/.vim

all: clean install
