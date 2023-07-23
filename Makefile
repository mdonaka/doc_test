.PHONY: genapi
genapi:
	sphinx-apidoc -f -o docs/source/reference packages

.PHONY: build
build: genapi
	sphinx-autobuild docs/source docs/_build/html
