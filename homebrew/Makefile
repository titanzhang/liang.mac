PWD = $(shell pwd)

install:
	ruby -e "$$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	brew update
	brew upgrade
	cat brewlist | xargs brew install

clean:

all: clean install
