.PHONY: genapi
genapi:
	sphinx-apidoc -f -o docs_src/source/reference packages

.PHONY: build
build: genapi
	sphinx-autobuild docs_src/source docs_src/_build/html
