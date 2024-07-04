##
# Project Title
#
# @file
# @version 0.1

up:
	python3 app/__init__.py

prepare:
	pyinstaller ci.spec

install:
	pip install -r requirements.txt

# end
