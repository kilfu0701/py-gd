clean:
	rm -rf ./build ./dist ./py_gd.egg-info

build:
	python setup.py sdist

upload:
	twine upload dist/*.tar.gz
